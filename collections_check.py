#! /usr/bin/python3
from plexapi.server import PlexServer
from pprint import pprint
from pymongo import MongoClient

#Set Up Plex connection
baseurl = 'http://192.168.1.65:32400'
token = 'xtKG_8iArPrvuftfNh-V'
plex = PlexServer(baseurl, token)

#Set up MongoDB
client = MongoClient('localhost', 27017)
db=client.plex_collections_test

def update():
    print ("Updating Database")
    libraries = plex.library.sections()
    for library in libraries:
        movie_sets = []
        if library.type == "movie":
            movies = library.search()
            for movie in movies:
                if movie.collections:
                    pprint (movie.title)
                    pprint (movie.collections)
                    movie_sets.append(movie.collections)
            result=db.counts.insert_one(movie_sets)

query = input("Do you want to update the database first? Y/N ")
if str(query).upper() == "Y":
    update()
