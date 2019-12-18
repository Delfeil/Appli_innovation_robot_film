create table films_only (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(35) NULL,
	duration time(8) NULL,
	release date NULL,
	restriction VARCHAR(35) NULL,
	synopsis VARCHAR(128) NULL
);

-- create table films_only (
-- 	id INTEGER PRIMARY KEY AUTOINCREMENT,
-- 	name VARCHAR(35) NULL,
-- 	duration TEXT() NULL,
-- 	release DATE() NULL,
-- 	restriction VARCHAR(35) NULL,
-- 	synopsis VARCHAR(128) NULL
-- );

	-- '1.44',
	-- 2019.11.20,
INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	'La reine des neiges 2',
	strftime('%H:%M', '01:44'),
	strftime('%Y-%m-%d', '2019-11-20'),
	"more6",
	"Pourquoi Elsa est-elle nee avec des pouvoirs magiques ? La jeune fille reve de l'apprendre, mais la reponse met son royaume en danger. Avec l'aide d'Anna, Kristoff, Olaf et Sven, Elsa entreprend un voyage aussi perilleux qu'extraordinaire. Dans La Reine des neiges, Elsa craignait que ses pouvoirs ne menacent le monde. Dans La Reine des neiges 2, elle espere qu'ils seront assez puissants pour le sauver..."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	'Joyeuse retraite',
	strftime('%H:%M', '01:37'),
	strftime('%Y-%m-%d', '2019-11-20'),
	"none",
	"L'heure de la retraite est enfin arrivee pour Philippe et Marilou ! Ils s'appretent a realiser leur reve : partir vivre sous le soleil du Portugal. Au revoir le travail, au revoir la famille, au revoir les emmerdes ! Ils pensaient enfin etre tranquilles... mais leur famille a d'autres projets pour eux !"
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	'Les Miserables',
	strftime('%H:%M', '01:42'),
	strftime('%Y-%m-%d', '2019-11-20'),
	"sensible",
	"Stephane, tout juste arrive de Cherbourg, integre la Brigade Anti-Criminalite de Montfermeil, dans le 93. Il va faire la rencontre de ses nouveaux coequipiers, Chris et Gwada, deux 'Bacqueux' d'experience. Il decouvre rapidement les tensions entre les differents groupes du quartier. Alors qu'ils se trouvent debordes lors d'une interpellation, un drone filme leurs moindres faits et gestes..."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	'Countdown',
	strftime('%H:%M', '01:30'),
	strftime('%Y-%m-%d', '2019-11-13'),
	"more12",
	"Voulez-vous savoir combien de temps il vous reste a vivre ? Telechargez l'appli Countdown ! Lorsque Quinn, une jeune infirmiere, telecharge cette application a la mode, elle decouvre qu'il ne lui reste que 3 jours a vivre. Elle doit trouver un moyen d'echapper a son sinistre destin avant la fin du compte a rebours."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	"J accuse",
	strftime('%H:%M', '02:12'),
	strftime('%Y-%m-%d', '2019-11-13'),
	"none",
	"Pendant les 12 annees qu'elle dura, l'Affaire Dreyfus dechira la France, provoquant un veritable seisme dans le monde entier. Dans cet immense scandale, le plus grand sans doute de la fin du XIXeme siecle, se melent erreur judiciaire, deni de justice et antisemitisme. L'affaire est racontee du point de vue du Colonel Picquart qui, une fois nomme a la tete du contre-espionnage, va decouvrir que les preuves contre le Capitaine Alfred Dreyfus avaient ete fabriquees. A partir de cet instant et au peril de sa carriere puis de sa vie, il n'aura de cesse d'identifier les vrais coupables et de rehabiliter Alfred Dreyfus."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	"Le Mans 66",
	strftime('%H:%M', '02:33'),
	strftime('%Y-%m-%d', '2019-11-13'),
	"none",
	"Base sur une histoire vraie, le film suit une equipe d'excentriques ingenieurs americains menes par le visionnaire Carroll Shelby et son pilote britannique Ken Miles, qui sont envoyes par Henry Ford II pour construire a partir de rien une nouvelle automobile qui doit detroner la Ferrari a la competition du Mans de 1966."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	"La belle epoque",
	strftime('%H:%M', '01:56'),
	strftime('%Y-%m-%d', '2019-11-06'),
	"none",
	"Victor, un sexagenaire desabuse, voit sa vie bouleversee le jour ou Antoine, un brillant entrepreneur, lui propose une attraction d u nouveau : melangeant artifices theatraux et reconstitution historique, cette entreprise propose a ses clients de replonger dans l'epoque de leur choix. Victor choisit alors de revivre la semaine la plus marquante de sa vie : celle ou, 40 ans plus tot, il rencontra le grand amour..."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	"Midway",
	strftime('%H:%M', '02:19'),
	strftime('%Y-%m-%d', '2019-11-06'),
	"none",
	"Apres la debacle de Pearl Harbor qui a laisse la flotte americaine devastee, la marine imperiale japonaise prepare une nouvelle attaque qui devrait eliminer definitivement les forces aeronavales restantes de son adversaire. La campagne du Pacifique va se jouer dans un petit atoll isole du Pacifique nord : Midway. L'amiral Nimitz, a la tete de la flotte americaine, voit cette bataille comme l'ultime chance de renverser la superiorite japonaise. Une course contre la montre s'engage alors pour Edwin Layton qui doit percer les codes secrets de la flotte japonaise et, grace aux renseignements, permettre aux pilotes de l'aviation americaine de faire face a la plus grande offensive jamais menee pendant ce conflit"
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	"Retour a Zombieland",
	strftime('%H:%M', '01:39'),
	strftime('%Y-%m-%d', '2019-10-30'),
	"sensible",
	"Le chaos regne partout dans le pays, depuis la Maison Blanche jusqu'aux petites villes les plus reculees. Nos quatre tueurs doivent desormais affronter de nouvelles races de zombies qui ont evolue en dix ans et une poignee de rescapes humains. Mais ce sont les conflits propres a cette ' famille ' improvisee qui restent les plus difficiles a gerer..."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	"Stephen King s Doctor Sleep",
	strftime('%H:%M', '02:32'),
	strftime('%Y-%m-%d', '2019-10-30'),
	"more12",
	"Un nouveau chapitre de Shining de Stanley Kubrick. Encore profondement marque par le traumatisme qu'il a vecu, enfant, a l'Overlook Hotel, Dan Torrance a du se battre pour tenter de trouver un semblant de serenite. Mais quand il rencontre Abra, courageuse adolescente aux dons extrasensoriels, ses vieux demons resurgissent. Car la jeune fille, consciente que Dan a les memes pouvoirs qu'elle, a besoin de son aide : elle cherche a lutter contre la redoutable Rose Claque et sa tribu du Noeud Vrai qui se nourrissent des dons d'innocents comme elle pour conquerir l'immortalite. Formant une alliance inattendue, Dan et Abra s'engagent dans un combat sans merci contre Rose. Face a l'innocence de la jeune fille et a sa maniere d'accepter son don, Dan n'a d'autre choix que de mobiliser ses propres pouvoirs, meme s'il doit affronter ses peurs et reveiller les fantomes du passe..."
);

INSERT INTO films_only(name, duration, release, restriction, synopsis) values(
	"Abominable",
	strftime('%H:%M', '01:37'),
	strftime('%Y-%m-%d', '2019-10-23'),
	"forAll",
	"Tout commence sur le toit d'un immeuble a Shanghai, avec l'improbable rencontre d'une jeune adolescente, l'intrepide Yi, avec un jeune Yeti. La jeune fille et ses amis Jin et Peng vont tenter de ramener chez lui celui qu'ils appellent desormais Everest, leur nouvel et etrange ami, afin qu'il puisse retrouver sa famille sur le toit du monde. Mais pour accomplir cette mission, notre trio de choc va devoir mener une course effrenee contre Burnish, un homme puissant qui a bien l'intention de capturer la creature car elle ressemble comme deux gouttes d'eau a celle qu'il avait fortuitement rencontree quand il etait enfant."
);

1|La reine des neiges 2|01:44|2019-11-20|...
2|Joyeuse retraite !|01:37|2019-11-20||...
3|Les Miserables|01:42|2019-11-20|...
4|Countdown|01:30|2019-11-13|...
5|J''accuse|02:12|2019-11-13||...
6|Le Mans 66|02:33|2019-11-13||...
7|La belle epoque|01:56|2019-11-06||...
8|Midway|02:19|2019-11-06||...
9|Retour a Zombieland|01:39|2019-10-30|...
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
