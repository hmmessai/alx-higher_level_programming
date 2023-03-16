-- Lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres WHERE tv_shows.title = "Dexter"
