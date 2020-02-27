import pandas
import helpers, spotify, db

get_newData = False

def get_artists(artists, songs):
    for song in songs:
        name = song['track']['artistName']
        info = spotify.get_artistByName(name)
        if (info != {}):
            artists.append({'id':info['artists']['items'][0]['id'],'name':name,'genres':info['artists']['items'][0]['genres']})
    return artists            

if (get_newData):
    artists = []
    for playlist in helpers.load_data('playlist')[0]['playlists']:
        get_artists(artists, playlist['items'])
        
    db.add_artists(artists)

    streaming_history = []
    for history in helpers.load_data('streaming_history'):
        frame = pandas.DataFrame(history)
        frame['endTime'] = pandas.to_datetime(frame['endTime']).dt.strftime('%W/%Y') #week and year
        
        for entry in (frame.groupby([frame['endTime'], frame['artistName']])['msPlayed'].sum()).items():
            genres = db.get_artist(entry[0][1])
            if (genres != None):
                streaming_history.append({'date':entry[0][0],'artist':entry[0][1],'genres':genres['genres'],'minutes':((entry[1] / 100) / 60)})

    db.add_history(streaming_history)

    top_artists = []

i = 1
for genre in db.get_genres():
    if (i == 1):
        ret = db.get_byGenre(genre)
        print(ret)
        i = 2