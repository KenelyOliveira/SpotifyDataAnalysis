import functions as f

# artists = {"name", "number_songs", "genres"}
artists = []

#getting artists from playlists
for playlist in f.load_data("playlist")["playlists"]:
    for artist in playlist["items"]:
        artists.append({"name": artist["track"]["artistName"]})

for a in artists:
    print (a)