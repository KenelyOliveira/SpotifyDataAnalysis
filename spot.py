import functions as f
import base64
import requests
import json
import pandas
from pymongo import MongoClient
from bson.code import Code
from pprint import pprint

# Get authorization to use their api
# Get artist info by name
# ###

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.SpotifyData

def persist_access_token(access_token):
    db.config.update_many({'expired':0}, {'$set':{'expired':1}})
    db.config.insert_one({'access_token':access_token,'expired':0})

def get_access_token():
    c = db.config.find_one({'expired':0})
    if (c != None):
        return c.get('access_token')
    return ''

def get_new_token():
    config = f.load_config()['gateway']
    headers = {'Authorization':'Basic %s' % (base64.encodebytes(('%s:%s' % (config['client_id'],config['client_secret'])).encode('utf-8')).decode().strip()).replace('\n', '')}
    payload = {'grant_type':'client_credentials'}
    response = requests.post(config['auth_url'], headers = headers, data = payload)
    print(json.loads(response.text)['access_token'])
    return json.loads(response.text)['access_token']

def get_artist(name):
    access_token = get_access_token()
    headers = {'Authorization':'Bearer %s' % access_token,'Accept':'application/json','Content-Type':'application/json'}
    response = requests.get(('https://api.spotify.com/v1/search?q=%s&type=artist' % f.format_query(name)), headers = headers)
    if (response.status_code == 200):
        return json.loads(response.text)
    if (response.status_code == 401):
        persist_access_token(get_new_token())
        return get_artist(name)
    return {}

get_newData = False

if (get_newData):
    #artists
    artists = []
    for playlist in f.load_data('playlist')['playlists']:
        for artist in playlist['items']:
            node = f.get_node(artists, artist['track']['artistName'])
            if (node == {}):
                name = artist['track']['artistName']
                info = get_artist(name)
                print(name)
                print(info)
                if (info != {}):
                    artists.append({'id':info['artists']['items'][0]['id'],'name':name,'genres':info['artists']['items'][0]['genres']})

    db.artists.insert_many(artists)
    
    #streaming_history
    streaming_history = []
    frame = pandas.DataFrame(f.load_data('streaming_history'))
    frame['endTime'] = pandas.to_datetime(frame['endTime']).dt.strftime('%b/%Y')
    history = frame.groupby([frame['endTime'], frame['artistName']])['msPlayed'].sum()

    result = []

    for data in history.items():
        date = data[0][0]
        artist = data[0][1]
        minutes = (data[1] / 100) / 60
        
        a = db.artists.find_one({'name': artist},{'_id': 0, 'genres': 1})
        if (a != None):
            mapper = Code('''
                        function () {
                            this.genres.forEach(function(z) {
                                emit(z, 1);
                            });
                        }
                        ''')
            
            reducer = Code('''
                        function (key, values) {
                            var total = 0;
                            for (var i = 0; i < values.length; i++) {
                                total += values[i];
                            }
                            return total;
                        }
                        ''')

            r = db.artists.map_reduce(mapper, reducer, 'count')
            for doc in r.find():
                x = minutes / doc['value']
                
                db.result.update_one({'date':date,'genre':doc['_id']},{'$set':{'minutes':x}}, upsert=True)