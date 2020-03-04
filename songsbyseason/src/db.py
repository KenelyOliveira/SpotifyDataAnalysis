from pymongo import MongoClient
from bson.code import Code

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.SpotifyData

def clear():
    db.artists.drop()
    db.streaming_history.drop()
    db.top_artists.drop()
    db.top_genres.drop()

def persist_access_token(access_token):
    db.config.update_many({'expired':0}, {'$set':{'expired':1}})
    db.config.insert_one({'access_token':access_token,'expired':0})

def get_access_token():
    config = db.config.find_one({'expired':0})
    if (config != None):
        return config.get('access_token')
    return None

def add_artists(artists):
    db.artists.insert_many(artists)

def get_artist(name):
    return db.artists.find_one({'name':name},{'_id': 0,'name': 1,'genres':1})

def add_history(history):
    db.streaming_history.insert_many(history)

def get_genres():
    return db.artists.distinct('genres')

def get_byGenre(genre):
    return list(db.streaming_history.find({'genres':{'$all':[genre]}}, {'_id': 0,'artist': 1,'genres':1}))

def add_top_artists(top_artists):
    db.top_artists.insert_many(top_artists)

def get_top_artists(date):
    return list(db.top_artists.find({'date':date},{'_id': 0}).sort('minutes',-1))

def add_top_genres(top_genres):
    db.top_genres.insert_many(top_genres)

def get_top_genres(date):
    return list(db.top_genres.find({'date':date},{'_id': 0}).sort('count',-1))