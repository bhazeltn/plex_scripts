#! /usr/bin/python3
from plexapi.server import PlexServer
from datetime import datetime, timedelta
import time
from pprint import pprint
from pymongo import MongoClient

#Set Up Plex connection
baseurl = 'http://home.hazeltonflix.ca:32400'
token = 'xtKG_8iArPrvuftfNh-V'
plex = PlexServer(baseurl, token)
 
#connect to MongoDB
client = MongoClient('localhost', 27017)
db=client.plex_test

print ("HazeltonFlix Media Counter")
movie_count = 0
episode_count = 0
show_count = 0
song_count = 0
count = 0
test_count = 0

#Check how long since last update
data = db.counts.find().sort([('timestamp', -1)]).limit(1)
for d in data:
    delta = datetime.now(tz=None) - d['timestamp']
    delta_as_time_obj = time.gmtime(delta.total_seconds())
    pprint ("It has been {0} since last update".format(
        time.strftime("%H:%M:%S", delta_as_time_obj)
    ))
query = input("Continue? Y/N ")
if str(query).upper() == "N":
    pprint ("Exiting")
    quit()

 
libraries = plex.library.sections()
print ("Counting Media...")
for library in libraries:
    if library.type == "movie":
        movie_count += library.totalSize
    if library.type == "show":
        show_count += library.totalSize
        episode_count += len(library.searchEpisodes())
    if library.type == "artist":
        artists = library.totalSize
        albums = len(library.searchAlbums())
        tracks = len(library.searchTracks())
print ("There are currently " + str(movie_count) + " movies")
print ("There are currently " + str(show_count) + " shows with " + str(episode_count) + " episodes")
print ("There are " + str(tracks) + " tracks in " + str(albums) + " albums by " + str(artists) + " artists")    
#print (datetime.now(tz=None))

count_data = {
    "movies": movie_count,
    "shows": show_count,
    "episodes": episode_count,
    "artists": artists,
    "albums": albums,
    "tracks": tracks,
    "timestamp": datetime.now(tz=None)
    }
#print (count_data)

result=db.counts.insert_one(count_data)