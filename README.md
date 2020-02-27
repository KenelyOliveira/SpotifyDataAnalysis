Analysis of how my music taste varies throughout the seasons, using Spotify's user data as input

V3:
	Group Streaming History by genre and total played
	Order result by Total Played and number of entries the genre appears (Spotify's API returns a list of genres by artist)
	Give a peso a cada um dos gêneros de acordo com:

Week: 52/2019

Artist			!	Minutes	!	Genres
Godsmack		|	16.40	!	["alternative metal","groove metal","nu metal","post-grunge","rap metal"]
Disturbed		!	42.76	!	["alternative metal","nu metal","post-grunge","rap metal"]
Black Sabbath	!	35.94	|	["album rock","birmingham metal","classic rock","hard rock","metal","rock","stoner rock","uk doom metal"]
Deep Purple		!	413.64	!	["album rock","blues rock","classic rock","hard rock","metal","psychedelic rock","rock"]
Led Zeppelin	!	307.45	|	["album rock","classic rock","hard rock","rock"]

For each genre: (ex, Alternative Metal)
EntriesByGenrer = 2
MinutesOfGenre = 59.16

Get genres in common with those EntriesByGenrer (union)

 * number of genres of its artist
		y = number of times EntriesByGenrer appears in the dataset

		w = z / s

		

V2:
	Re-fetch Streaming History by Week/Year
	Authenticate in Spotify's public API and fetch artist's data
		Update Artists dataset with the resulting genres
	Persist results in MongoDB
	Refactor project

V1:
	Load previously downloaded data and consolidate:
		Artist and genres 
		Streaming History by Month/Year
	Authenticate in LastFM's public API and fetch artist's info
		Update Artist dataset with the resulting genres

