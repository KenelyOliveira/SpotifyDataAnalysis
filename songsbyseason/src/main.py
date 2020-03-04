import pandas
import helpers, spotify, db

get_newData = True

def get_artists(artists, songs):
    for song in songs:
        name = song['track']['artistName']
        info = spotify.get_artistByName(name)
        if (info != {}):
            artists.append({'id':info['artists']['items'][0]['id'],'name':name,'genres':info['artists']['items'][0]['genres']})
    return artists            

if (get_newData):
    
    print('Cleaning collections...')
    db.clear()
    
    artists = []

    print('Getting artists list...')
    for playlist in helpers.load_data('playlist')[0]['playlists']:
        get_artists(artists, playlist['items'])
        
    db.add_artists(artists)
    print('Done getting artists!')
    
    streaming_history = []
    top_artists = []
    top_genres = []

    print('Getting streaming history...')
    for history in helpers.load_data('streaming_history'):
        frame = pandas.DataFrame(history)
        frame['endTime'] = pandas.to_datetime(frame['endTime']).dt.strftime('%W/%Y') #week and year
        
        for entry in (frame.groupby([frame['endTime'], frame['artistName']])['msPlayed'].sum()).items():
            genres = db.get_artist(entry[0][1])
            if (genres != None):
                streaming_history.append({'date':entry[0][0],'artist':entry[0][1],'genres':genres['genres'],'minutes':((entry[1] / 100) / 60)})
                for genre in genres['genres']:
                    key = ('%s:%s' % (entry[0][0],genre))
                    node = helpers.get_node(top_genres, 'key', key)
                    if (node == None):
                        top_genres.append({'key':key,'date':entry[0][0],'genre':genre,'count':1})
                    else:
                        node['count'] = int(node['count']) + 1

                key = ('%s:%s' % (entry[0][0],entry[0][1]))
                node = helpers.get_node(top_artists, 'key', key)
                if (node == None):
                    top_artists.append({'key':key,'date':entry[0][0],'artist':entry[0][1],'minutes': float(((entry[1] / 100) / 60))})
                else:
                    node['minutes'] = float(node['minutes']) + float(((entry[1] / 100) / 60))

    db.add_history(streaming_history)
    db.add_top_artists(top_artists)
    db.add_top_genres(top_genres)

    print('Done getting streaming history!')