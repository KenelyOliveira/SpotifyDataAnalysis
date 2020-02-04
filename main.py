import json
import functions as f

artists = []
get_newData = False

if (get_newData):

    #getting artists from playlists
    for playlist in f.load_data("playlist")["playlists"]:
        for artist in playlist["items"]:
            node = f.get_node(artists, artist["track"]["artistName"])
            if (node == {}):
                artists.append({"name": artist["track"]["artistName"]})
            # if (node == {}):
            #     artists.append({"name": artist["track"]["artistName"], "songs": [ artist["track"]["trackName"] ]})
            # else:
            #     node["songs"].append(artist["track"]["trackName"])

    #getting musical genre by artist
    for a in artists:
        tags = json.loads(f.get_artistByGenre(a["name"]).text)["artist"]["tags"]["tag"]
        new_genre = True
        for tag in tags:
            node = f.get_node(artists, a["name"])
            if new_genre:
                node["genres"] = []
            node["genres"].append(tag["name"]) 
            new_genre = False

    with open("consolidated_data/playlist.json", "w") as output:
        json.dump(artists, output)

with open("consolidated_data/playlist.json", encoding = "utf8") as c:
    consolidated_data = json.load(c)

streaming_history = []

i = 1

#combining musical info with streaming history

# with open("consolidated_data/streaming_history.json", "w") as output:
#     json.dump(f.load_data("streaming_history"), output)

for history in f.load_data("streaming_history"):
    if i < 5:
        genres = f.get_node(consolidated_data, history["artistName"])
        print(history["artistName"])
        streaming_history.append({"artist": history["artistName"], "song": history["trackName"], "ms": history["msPlayed"], "genres": genres })
        i = i +1

# f.print_json(streaming_history)