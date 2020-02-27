Analysis of how my music taste varies throughout the seasons, using Spotify's user data as input.

V4: 
	Create page to show the results

V3:
	Group Streaming History by genre and total played
	Order result by Total Played and number of entries the genre appears (Spotify's API returns a list of genres by artist)

V2:
	Re-fetch Streaming History by Week/Year
	Authenticate in Spotify's public API and fetch artist's data
		Update Artists dataset with the resulting genres
	Persist results in MongoDB
	Refactor project

V1:
	Load previously downloaded data and consolidate by:
		Artist and genres 
		Streaming History by Month/Year
	Authenticate in LastFM's public API and fetch artist's info
		Update Artist dataset with the resulting genres

