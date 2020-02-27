from pymongo import MongoClient
from bson.code import Code

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.SpotifyData

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

def oi():
    db.streaming_history.distinct('date')
    db.streaming_history.find({'genre':{'$exists':False}}).sort({'date':1})