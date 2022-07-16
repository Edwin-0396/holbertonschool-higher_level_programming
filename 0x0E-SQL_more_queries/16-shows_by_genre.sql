-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT
	tv_shows.title,
	tv_genres.name
FROM
	tv_shows
	-- left join several tables
	LEFT JOIN
	(tv_genres, tv_show_genres)
	-- gruop several condictions
	ON
	(tv_shows.id = tv_show_genres.show_id
	AND
	tv_genres.id = tv_show_genres.genre_id)
ORDER BY
	tv_shows.title, tv_genres.name
;