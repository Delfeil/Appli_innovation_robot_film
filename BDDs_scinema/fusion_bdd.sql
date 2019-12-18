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

1|La reine des neiges 2|01:44|2019-11-20|Tous publics à partir de 6 ans|Pourquoi Elsa est-elle née avec des pouvoirs magiques ? La jeune fille rêve de l'apprendre, mais la réponse met son royaume en danger. Avec l'aide d'Anna, Kristoff, Olaf et Sven, Elsa entreprend un voyage aussi périlleux qu'extraordinaire. Dans La Reine des neiges, Elsa craignait que ses pouvoirs ne menacent le monde. Dans La Reine des neiges 2, elle espère qu'ils seront assez puissants pour le sauver...|animation
2|Joyeuse retraite !|01:37|2019-11-20||L'heure de la retraite est enfin arrivée pour Philippe et Marilou ! Ils s'apprêtent à réaliser leur rêve : partir vivre sous le soleil du Portugal. Au revoir le travail, au revoir la famille, au revoir les emmerdes ! Ils pensaient enfin être tranquilles... mais leur famille a d'autres projets pour eux !|comédie
3|Les Misérables|01:42|2019-11-20|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|Stéphane, tout juste arrivé de Cherbourg, intègre la Brigade Anti-Criminalité de Montfermeil, dans le 93. Il va faire la rencontre de ses nouveaux coéquipiers, Chris et Gwada, deux 'Bacqueux' d'expérience. Il découvre rapidement les tensions entre les différents groupes du quartier. Alors qu'ils se trouvent débordés lors d'une interpellation, un drone filme leurs moindres faits et gestes...|film noir-policier
4|Les Misérables|01:42|2019-11-20|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|Stéphane, tout juste arrivé de Cherbourg, intègre la Brigade Anti-Criminalité de Montfermeil, dans le 93. Il va faire la rencontre de ses nouveaux coéquipiers, Chris et Gwada, deux 'Bacqueux' d'expérience. Il découvre rapidement les tensions entre les différents groupes du quartier. Alors qu'ils se trouvent débordés lors d'une interpellation, un drone filme leurs moindres faits et gestes...|drame
5|Countdown|01:30|2019-11-13|Interdit aux -12 ans|Voulez-vous savoir combien de temps il vous reste à vivre ? Téléchargez l'appli Countdown ! Lorsque Quinn, une jeune infirmière, télécharge cette application à la mode, elle découvre qu'il ne lui reste que 3 jours à vivre. Elle doit trouver un moyen d'échapper à son sinistre destin avant la fin du compte à rebours.|épouvante-horreur
6|J'accuse|02:12|2019-11-13||Pendant les 12 années qu'elle dura, l'Affaire Dreyfus déchira la France, provoquant un véritable séisme dans le monde entier. Dans cet immense scandale, le plus grand sans doute de la fin du XIXème siècle, se mêlent erreur judiciaire, déni de justice et antisémitisme. L'affaire est racontée du point de vue du Colonel Picquart qui, une fois nommé à la tête du contre-espionnage, va découvrir que les preuves contre le Capitaine Alfred Dreyfus avaient été fabriquées. A partir de cet instant et au péril de sa carrière puis de sa vie, il n'aura de cesse d'identifier les vrais coupables et de réhabiliter Alfred Dreyfus.|historique
7|J'accuse|02:12|2019-11-13||Pendant les 12 années qu'elle dura, l'Affaire Dreyfus déchira la France, provoquant un véritable séisme dans le monde entier. Dans cet immense scandale, le plus grand sans doute de la fin du XIXème siècle, se mêlent erreur judiciaire, déni de justice et antisémitisme. L'affaire est racontée du point de vue du Colonel Picquart qui, une fois nommé à la tête du contre-espionnage, va découvrir que les preuves contre le Capitaine Alfred Dreyfus avaient été fabriquées. A partir de cet instant et au péril de sa carrière puis de sa vie, il n'aura de cesse d'identifier les vrais coupables et de réhabiliter Alfred Dreyfus.|drame
8|J'accuse|02:12|2019-11-13||Pendant les 12 années qu'elle dura, l'Affaire Dreyfus déchira la France, provoquant un véritable séisme dans le monde entier. Dans cet immense scandale, le plus grand sans doute de la fin du XIXème siècle, se mêlent erreur judiciaire, déni de justice et antisémitisme. L'affaire est racontée du point de vue du Colonel Picquart qui, une fois nommé à la tête du contre-espionnage, va découvrir que les preuves contre le Capitaine Alfred Dreyfus avaient été fabriquées. A partir de cet instant et au péril de sa carrière puis de sa vie, il n'aura de cesse d'identifier les vrais coupables et de réhabiliter Alfred Dreyfus.|thriller
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