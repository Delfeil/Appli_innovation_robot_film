create table films (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(35) NULL,
	duration time(8) NULL,
	release date NULL,
	restriction VARCHAR(35) NULL,
	synopsis VARCHAR(128) NULL,
	genre VARCHAR(35) NULL
);

-- create table films (
-- 	id INTEGER PRIMARY KEY AUTOINCREMENT,
-- 	name VARCHAR(35) NULL,
-- 	duration TEXT() NULL,
-- 	release DATE() NULL,
-- 	restriction VARCHAR(35) NULL,
-- 	synopsis VARCHAR(128) NULL
-- );

	-- '1.44',
	-- 2019.11.20,
INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	'La reine des neiges 2',
	strftime('%H:%M', '01:44'),
	strftime('%Y-%m-%d', '2019-11-20'),
	"Tous publics à partir de 6 ans",
	"animation",
	"Pourquoi Elsa est-elle née avec des pouvoirs magiques ? La jeune fille rêve de l'apprendre, mais la réponse met son royaume en danger. Avec l'aide d'Anna, Kristoff, Olaf et Sven, Elsa entreprend un voyage aussi périlleux qu'extraordinaire. Dans La Reine des neiges, Elsa craignait que ses pouvoirs ne menacent le monde. Dans La Reine des neiges 2, elle espère qu'ils seront assez puissants pour le sauver...",
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	'Joyeuse retraite !',
	strftime('%H:%M', '01:37'),
	strftime('%Y-%m-%d', '2019-11-20'),
	"",
	"Comédie",
	"L'heure de la retraite est enfin arrivée pour Philippe et Marilou ! Ils s'apprêtent à réaliser leur rêve : partir vivre sous le soleil du Portugal. Au revoir le travail, au revoir la famille, au revoir les emmerdes ! Ils pensaient enfin être tranquilles... mais leur famille a d'autres projets pour eux !"
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	'Les Misérables',
	strftime('%H:%M', '01:42'),
	strftime('%Y-%m-%d', '2019-11-20'),
	"Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs",
	"Drame",
	"Stéphane, tout juste arrivé de Cherbourg, intègre la Brigade Anti-Criminalité de Montfermeil, dans le 93. Il va faire la rencontre de ses nouveaux coéquipiers, Chris et Gwada, deux 'Bacqueux' d'expérience. Il découvre rapidement les tensions entre les différents groupes du quartier. Alors qu'ils se trouvent débordés lors d'une interpellation, un drone filme leurs moindres faits et gestes..."
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	'Countdown',
	strftime('%H:%M', '01:30'),
	strftime('%Y-%m-%d', '2019-11-13'),
	"Interdit aux -12 ans",
	"horeur",
	"Voulez-vous savoir combien de temps il vous reste à vivre ? Téléchargez l'appli Countdown ! Lorsque Quinn, une jeune infirmière, télécharge cette application à la mode, elle découvre qu'il ne lui reste que 3 jours à vivre. Elle doit trouver un moyen d'échapper à son sinistre destin avant la fin du compte à rebours."
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	"J'accuse",
	strftime('%H:%M', '02:12'),
	strftime('%Y-%m-%d', '2019-11-13'),
	"",
	"historique",
	"Pendant les 12 années qu'elle dura, l'Affaire Dreyfus déchira la France, provoquant un véritable séisme dans le monde entier. Dans cet immense scandale, le plus grand sans doute de la fin du XIXème siècle, se mêlent erreur judiciaire, déni de justice et antisémitisme. L'affaire est racontée du point de vue du Colonel Picquart qui, une fois nommé à la tête du contre-espionnage, va découvrir que les preuves contre le Capitaine Alfred Dreyfus avaient été fabriquées. A partir de cet instant et au péril de sa carrière puis de sa vie, il n'aura de cesse d'identifier les vrais coupables et de réhabiliter Alfred Dreyfus."
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	"Le Mans 66",
	strftime('%H:%M', '02:33'),
	strftime('%Y-%m-%d', '2019-11-13'),
	"",
	"biopic",
	"Basé sur une histoire vraie, le film suit une équipe d'excentriques ingénieurs américains menés par le visionnaire Carroll Shelby et son pilote britannique Ken Miles, qui sont envoyés par Henry Ford II pour construire à partir de rien une nouvelle automobile qui doit détrôner la Ferrari à la compétition du Mans de 1966."
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	"La belle époque",
	strftime('%H:%M', '01:56'),
	strftime('%Y-%m-%d', '2019-11-06'),
	"",
	"comédie",
	"Victor, un sexagénaire désabusé, voit sa vie bouleversée le jour où Antoine, un brillant entrepreneur, lui propose une attraction d'genre, u nouveau : mélangeant artifices théâtraux et reconstitution historique, cette entreprise propose à ses clients de replonger dans l'époque de leur choix. Victor choisit alors de revivre la semaine la plus marquante de sa vie : celle où, 40 ans plus tôt, il rencontra le grand amour..."
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	"Midway",
	strftime('%H:%M', '02:19'),
	strftime('%Y-%m-%d', '2019-11-06'),
	"",
	"action",
	"Après la débâcle de Pearl Harbor qui a laissé la flotte américaine dévastée, la marine impériale japonaise prépare une nouvelle attaque qui devrait éliminer définitivement les forces aéronavales restantes de son adversaire. La campagne du Pacifique va se jouer dans un petit atoll isolé du Pacifique nord : Midway. L'amiral Nimitz, à la tête de la flotte américaine, voit cette bataille comme l'ultime chance de renverser la supériorité japonaise. Une course contre la montre s'engage alors pour Edwin Layton qui doit percer les codes secrets de la flotte japonaise et, grâce aux renseignements, permettre aux pilotes de l'aviation américaine de faire face à la plus grande offensive jamais menée pendant ce conflit"
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	"Retour à Zombieland",
	strftime('%H:%M', '01:39'),
	strftime('%Y-%m-%d', '2019-10-30'),
	"Des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs",
	"comédie",
	"Le chaos règne partout dans le pays, depuis la Maison Blanche jusqu'aux petites villes les plus reculées. Nos quatre tueurs doivent désormais affronter de nouvelles races de zombies qui ont évolué en dix ans et une poignée de rescapés humains. Mais ce sont les conflits propres à cette « famille » improvisée qui restent les plus difficiles à gérer..."
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	"Stephen King's Doctor Sleep",
	strftime('%H:%M', '02:32'),
	strftime('%Y-%m-%d', '2019-10-30'),
	"Interdit aux -12 ans",
	"thriller",
	"Un nouveau chapitre de Shining de Stanley Kubrick. Encore profondément marqué par le traumatisme qu'il a vécu, enfant, à l'Overlook Hotel, Dan Torrance a dû se battre pour tenter de trouver un semblant de sérénité. Mais quand il rencontre Abra, courageuse adolescente aux dons extrasensoriels, ses vieux démons resurgissent. Car la jeune fille, consciente que Dan a les mêmes pouvoirs qu'elle, a besoin de son aide : elle cherche à lutter contre la redoutable Rose Claque et sa tribu du Noeud Vrai qui se nourrissent des dons d'innocents comme elle pour conquérir l'immortalité. Formant une alliance inattendue, Dan et Abra s'engagent dans un combat sans merci contre Rose. Face à l'innocence de la jeune fille et à sa manière d'accepter son don, Dan n'a d'autre choix que de mobiliser ses propres pouvoirs, même s'il doit affronter ses peurs et réveiller les fantômes du passé..."
);

INSERT INTO films(name, duration, release, restriction, genre, synopsis) values(
	"Abominable",
	strftime('%H:%M', '01:37'),
	strftime('%Y-%m-%d', '2019-10-23'),
	"Tous publics",
	"animation",
	"Tout commence sur le toit d'un immeuble à Shanghai, avec l'improbable rencontre d'une jeune adolescente, l'intrépide Yi, avec un jeune Yeti. La jeune fille et ses amis Jin et Peng vont tenter de ramener chez lui celui qu'ils appellent désormais Everest, leur nouvel et étrange ami, afin qu'il puisse retrouver sa famille sur le toit du monde. Mais pour accomplir cette mission, notre trio de choc va devoir mener une course effrénée contre Burnish, un homme puissant qui a bien l'intention de capturer la créature car elle ressemble comme deux gouttes d'eau à celle qu'il avait fortuitement rencontrée quand il était enfant."
);

1|La reine des neiges 2|01:44|2019-11-20|...
2|Joyeuse retraite !|01:37|2019-11-20||...
3|Les Misérables|01:42|2019-11-20|...
4|Countdown|01:30|2019-11-13|...
5|J''accuse|02:12|2019-11-13||...
6|Le Mans 66|02:33|2019-11-13||...
7|La belle époque|01:56|2019-11-06||...
8|Midway|02:19|2019-11-06||...
9|Retour à Zombieland|01:39|2019-10-30|...
10|Stephen King''s Doctor Sleep|02:32|2019-10-30|...
11|Abominable|01:37|2019-10-23|...


CREATE TABLE KUSTOM (
id VARCHAR(8) NULL,
name VARCHAR(35) NULL,
kind VARCHAR(8) NULL,
energy VARCHAR(8) NULL,
fatness VARCHAR(6) NULL,
saltiness VARCHAR(8) NULL,
sweetness VARCHAR(6) NULL,
meat VARCHAR(7) NULL,
hasbacon VARCHAR(2) NULL,
hascheese VARCHAR(2) NULL,
ishappymealavailable VARCHAR(2) NULL,
ishappymealonly VARCHAR(2) NULL,
pieces VARCHAR(2) NULL
);
