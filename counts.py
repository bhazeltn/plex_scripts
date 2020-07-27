#! /usr/bin/python3
from plexapi.server import PlexServer
from datetime import datetime

#Set Up Plex connection
baseurl = 'http://home.hazeltonflix.ca:32400'
token = 'xtKG_8iArPrvuftfNh-V'
plex = PlexServer(baseurl, token)
 
print ("HazeltonFlix Media Counter")
movie_count = 0
episode_count = 0
show_count = 0
song_count = 0
count = 0
test_count = 0
 
 
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
 
print (datetime.now(tz=None))

