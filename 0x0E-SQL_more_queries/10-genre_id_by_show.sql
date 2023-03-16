-- Lists all shows contained in hbtn_od_tvshows that have at least 1 genre linked
SELECT tv_shows.title, tv_show_genres.genere_id
FROM tv_shows
	INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show.genres.genre_id ASC;
