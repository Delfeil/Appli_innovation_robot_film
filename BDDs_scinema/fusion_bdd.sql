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

1|Joyeuse retraite !|01:37|2019-11-20||L'heure de la retraite est enfin arrivée pour Philippe et Marilou ! Ils s'apprêtent à réaliser leur rêve : partir vivre sous le soleil du Portugal. Au revoir le travail, au revoir la famille, au revoir les emmerdes ! Ils pensaient enfin être tranquilles... mais leur famille a d'autres projets pour eux !|animation
2|Joyeuse retraite !|01:37|2019-11-20||L'heure de la retraite est enfin arrivée pour Philippe et Marilou ! Ils s'apprêtent à réaliser leur rêve : partir vivre sous le soleil du Portugal. Au revoir le travail, au revoir la famille, au revoir les emmerdes ! Ils pensaient enfin être tranquilles... mais leur famille a d'autres projets pour eux !|guerre
3|Les Misérables|01:42|2019-11-20|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|Stéphane, tout juste arrivé de Cherbourg, intègre la Brigade Anti-Criminalité de Montfermeil, dans le 93. Il va faire la rencontre de ses nouveaux coéquipiers, Chris et Gwada, deux 'Bacqueux' d'expérience. Il découvre rapidement les tensions entre les différents groupes du quartier. Alors qu'ils se trouvent débordés lors d'une interpellation, un drone filme leurs moindres faits et gestes...|comédie
4|Les Misérables|01:42|2019-11-20|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|Stéphane, tout juste arrivé de Cherbourg, intègre la Brigade Anti-Criminalité de Montfermeil, dans le 93. Il va faire la rencontre de ses nouveaux coéquipiers, Chris et Gwada, deux 'Bacqueux' d'expérience. Il découvre rapidement les tensions entre les différents groupes du quartier. Alors qu'ils se trouvent débordés lors d'une interpellation, un drone filme leurs moindres faits et gestes...|aventure
5|Countdown|01:30|2019-11-13|Interdit aux -12 ans|Voulez-vous savoir combien de temps il vous reste à vivre ? Téléchargez l'appli Countdown ! Lorsque Quinn, une jeune infirmière, télécharge cette application à la mode, elle découvre qu'il ne lui reste que 3 jours à vivre. Elle doit trouver un moyen d'échapper à son sinistre destin avant la fin du compte à rebours.|drame
6|J'accuse|02:12|2019-11-13||Pendant les 12 années qu'elle dura, l'Affaire Dreyfus déchira la France, provoquant un véritable séisme dans le monde entier. Dans cet immense scandale, le plus grand sans doute de la fin du XIXème siècle, se mêlent erreur judiciaire, déni de justice et antisémitisme. L'affaire est racontée du point de vue du Colonel Picquart qui, une fois nommé à la tête du contre-espionnage, va découvrir que les preuves contre le Capitaine Alfred Dreyfus avaient été fabriquées. A partir de cet instant et au péril de sa carrière puis de sa vie, il n'aura de cesse d'identifier les vrais coupables et de réhabiliter Alfred Dreyfus.|épouvante-horreur
7|Le Mans 66|02:33|2019-11-13||Basé sur une histoire vraie, le film suit une équipe d'excentriques ingénieurs américains menés par le visionnaire Carroll Shelby et son pilote britannique Ken Miles, qui sont envoyés par Henry Ford II pour construire à partir de rien une nouvelle automobile qui doit détrôner la Ferrari à la compétition du Mans de 1966.|historique
8|La belle époque|01:56|2019-11-06||Victor, un sexagénaire désabusé, voit sa vie bouleversée le jour où Antoine, un brillant entrepreneur, lui propose une attraction d'genre, u nouveau : mélangeant artifices théâtraux et reconstitution historique, cette entreprise propose à ses clients de replonger dans l'époque de leur choix. Victor choisit alors de revivre la semaine la plus marquante de sa vie : celle où, 40 ans plus tôt, il rencontra le grand amour...|biopic
9|Midway|02:19|2019-11-06||Après la débâcle de Pearl Harbor qui a laissé la flotte américaine dévastée, la marine impériale japonaise prépare une nouvelle attaque qui devrait éliminer définitivement les forces aéronavales restantes de son adversaire. La campagne du Pacifique va se jouer dans un petit atoll isolé du Pacifique nord : Midway. L'amiral Nimitz, à la tête de la flotte américaine, voit cette bataille comme l'ultime chance de renverser la supériorité japonaise. Une course contre la montre s'engage alors pour Edwin Layton qui doit percer les codes secrets de la flotte japonaise et, grâce aux renseignements, permettre aux pilotes de l'aviation américaine de faire face à la plus grande offensive jamais menée pendant ce conflit|comédie
10|Retour à Zombieland|01:39|2019-10-30|Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs|Le chaos règne partout dans le pays, depuis la Maison Blanche jusqu'aux petites villes les plus reculées. Nos quatre tueurs doivent désormais affronter de nouvelles races de zombies qui ont évolué en dix ans et une poignée de rescapés humains. Mais ce sont les conflits propres à cette « famille » improvisée qui restent les plus difficiles à gérer...|action
11|Stephen King's Doctor Sleep|02:32|2019-10-30|Interdit aux -12 ans|Un nouveau chapitre de Shining de Stanley Kubrick. Encore profondément marqué par le traumatisme qu'il a vécu, enfant, à l'Overlook Hotel, Dan Torrance a dû se battre pour tenter de trouver un semblant de sérénité. Mais quand il rencontre Abra, courageuse adolescente aux dons extrasensoriels, ses vieux démons resurgissent. Car la jeune fille, consciente que Dan a les mêmes pouvoirs qu'elle, a besoin de son aide : elle cherche à lutter contre la redoutable Rose Claque et sa tribu du Noeud Vrai qui se nourrissent des dons d'innocents comme elle pour conquérir l'immortalité. Formant une alliance inattendue, Dan et Abra s'engagent dans un combat sans merci contre Rose. Face à l'innocence de la jeune fille et à sa manière d'accepter son don, Dan n'a d'autre choix que de mobiliser ses propres pouvoirs, même s'il doit affronter ses peurs et réveiller les fantômes du passé...|comédie
12|Abominable|01:37|2019-10-23|Tous publics|Tout commence sur le toit d'un immeuble à Shanghai, avec l'improbable rencontre d'une jeune adolescente, l'intrépide Yi, avec un jeune Yeti. La jeune fille et ses amis Jin et Peng vont tenter de ramener chez lui celui qu'ils appellent désormais Everest, leur nouvel et étrange ami, afin qu'il puisse retrouver sa famille sur le toit du monde. Mais pour accomplir cette mission, notre trio de choc va devoir mener une course effrénée contre Burnish, un homme puissant qui a bien l'intention de capturer la créature car elle ressemble comme deux gouttes d'eau à celle qu'il avait fortuitement rencontrée quand il était enfant.|thriller
