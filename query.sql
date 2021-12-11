SELECT artist_name, COUNT(painting_name) FROM the_most_famous_painting LEFT JOIN  artist ON the_most_famous_painting.painting_id =  artist.artist_id GROUP BY artist_name

SELECT genre, COUNT(genre_id) FROM genre INNER JOIN bio USING(genre_id) GROUP BY genre

SELECT genre_name, COUNT(about_bio) FROM bio LEFT JOIN genre ON bio.genre_id = genre.genre_id GROUP BY genre_name