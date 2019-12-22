create table relation_genres_films (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_film INTEGER,
	id_genre INTEGER
);

-- Lareine des eniges annimation
INSERT INTO relation_genres_films(id_film, id_genre) values(
	1, 5
);

--  Joyeuse retraite !, Comédie
INSERT INTO relation_genres_films(id_film, id_genre) values(
	2, 3
);

-- Les Misérables - film noir policier
INSERT INTO relation_genres_films(id_film, id_genre) values(
	3, 7 
);

-- Les Misérables - Drame
INSERT INTO relation_genres_films(id_film, id_genre) values(
	3, 8
);

-- Countdown - horeur
INSERT INTO relation_genres_films(id_film, id_genre) values(
	4, 9
);

-- J'accuse - historique
INSERT INTO relation_genres_films(id_film, id_genre) values(
	5, 10
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	5, 8
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	5, 11
);

-- Le Mans 66 - Biopic
INSERT INTO relation_genres_films(id_film, id_genre) values(
	6, 12
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	6, 8
);

-- La belle époque - comédie
INSERT INTO relation_genres_films(id_film, id_genre) values(
	7, 3
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	7, 8
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	7, 13
);

-- Midway - action
INSERT INTO relation_genres_films(id_film, id_genre) values(
	8, 14
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	8, 10
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	8, 15
);

-- Retour à Zombieland - comédie
INSERT INTO relation_genres_films(id_film, id_genre) values(
	9, 3
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	9, 9
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	9, 14
);

-- Stephen King's Doctor Sleep - thriller
INSERT INTO relation_genres_films(id_film, id_genre) values(
	10, 11
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	10, 16
);

-- Abominable - animation
INSERT INTO relation_genres_films(id_film, id_genre) values(
	11, 5
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	11, 4
);

INSERT INTO relation_genres_films(id_film, id_genre) values(
	11, 3
);

1|1|5
2|1|15
3|2|3
4|2|4
5|3|8
6|4|9
7|5|10
8|6|12
9|7|3
10|8|14
11|9|3
12|10|11
13|11|5

