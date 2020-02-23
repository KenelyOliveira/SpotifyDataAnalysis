# import json
# import pandas
import songsbyseason.helpers as helpers

print(helpers.format_query('Olá mundo'))
# get_newData = False
# print(helpers.format_query('Olá mundo'))

# def get_artists(artists, songs):
#     for song in songs:
#         name = song['track']['artistName']
#         info = spotify.get_artistByName(name)
#         if (info != {}):
#             artists.append({'id':info['artists']['items'][0]['id'],'name':name,'genres':info['artists']['items'][0]['genres']})
#     return artists            

# if (get_newData):
#     artists = []
#     for playlist in helpers.load_data('playlist')[0]['playlists']:
#         get_artists(artists, playlist['items'])
        
#     db.add_artists(artists)
    
#     frame = pandas.DataFrame(helpers.load_data('streaming_history'))
#     frame['endTime'] = pandas.to_datetime(frame['endTime']).dt.strftime('%W/%Y')
#     streaming_history = frame.groupby([frame['endTime'], frame['artistName']])['msPlayed'].sum().items()

#     db.add_history(streaming_history)


# for entry in streaming_history:
#     date = entry[0][0]
#     artist = entry[0][1]
#     minutes = (entry[1] / 100) / 60

#     print('%s - %s' % date, artist)
    
#     # a = db.artists.find_one({'name': artist},{'_id': 0, 'genres': 1})
#     # if (a != None):
#     #     mapper = Code('''
#     #                 function () {
#     #                     this.genres.forEach(function(z) {
#     #                         emit(z, 1);
#     #                     });
#     #                 }
#     #                 ''')
        
#     #     reducer = Code('''
#     #                 function (key, values) {
#     #                     var total = 0;
#     #                     for (var i = 0; i < values.length; i++) {
#     #                         total += values[i];
#     #                     }
#     #                     return total;
#     #                 }
#     #                 ''')

#     #     r = db.artists.map_reduce(mapper, reducer, 'count')
#     #     for doc in r.find():
#     #         x = minutes / doc['value']
            
#     #         db.result.update_one({'date':date,'genre':doc['_id']},{'$set':{'minutes':x}}, upsert=True)