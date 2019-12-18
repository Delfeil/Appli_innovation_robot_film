create table films_genres (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(35) NULL,
	duration time(8) NULL,
	release date NULL,
	restriction VARCHAR(35) NULL,
	synopsis VARCHAR(128) NULL,
	genre VARCHAR(35) NULL
);



-- https://stackoverflow.com/questions/80801/how-can-i-merge-many-sqlite-databases
-- https://stackoverflow.com/questions/18712761/merging-two-tables-in-sqlite-from-different-database
-- https://www.sqlitetutorial.net/sqlite-transaction/
-- https://gist.github.com/jkpr/204f5f5318080ae5962d8272cce1eea4

attach 'films.db' as films;  
attach 'rel-film-genre.db' as relation_genres_films;
attach 'genres.db' as genres;

BEGIN;

INSERT INTO films_genres(name, duration, release, restriction, synopsis, genre) select f.name, f.duration, f.release, f.restriction, f.synopsis, g.genre
from films f
	JOIN relation_genres_films.relation_genres_films r ON r.id_film = f.id
	JOIN genres g ON r.id_genre = g.id;

COMMIT;

1|La reine des neiges 2|01:44|2019-11-20|...|animation
2|Joyeuse retraite !|01:37|2019-11-20||...|comédie
3|Les Misérables|01:42|2019-11-20|...|film noir-policier
4|Les Misérables|01:42|2019-11-20|...|drame
5|Countdown|01:30|2019-11-13|Interdit aux -12 ans|..épouvante-horreur
6|J'accuse|02:12|2019-11-13||...|historique
7|J'accuse|02:12|2019-11-13||...|drame
8|J'accuse|02:12|2019-11-13||...|thriller
9|Le Mans 66|02:33|2019-11-13||...|biopic
10|Le Mans 66|02:33|2019-11-13||...|drame
11|La belle époque|01:56|2019-11-06||...|comédie
12|La belle époque|01:56|2019-11-06||...|drame
13|La belle époque|01:56|2019-11-06||...|romance
14|Midway|02:19|2019-11-06||...|action
15|Midway|02:19|2019-11-06||...|historique
16|Midway|02:19|2019-11-06||...|guerre
17|Retour à Zombieland|01:39|2019-10-30|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|...|comédie
18|Retour à Zombieland|01:39|2019-10-30|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|...|épouvante-horreur
19|Retour à Zombieland|01:39|2019-10-30|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|...|action
20|Stephen King's Doctor Sleep|02:32|2019-10-30|...|thriller
21|Stephen King's Doctor Sleep|02:32|2019-10-30|...|fantastique
22|Abominable|01:37|2019-10-23|Tous publics|...|animation
23|Abominable|01:37|2019-10-23|Tous publics|...|aventure
24|Abominable|01:37|2019-10-23|Tous publics|...|comédie
