# Appli_innovation_robot_film 2019-2020

Contacter fabrice.lefevre@univ-avignon, 2019

## Installation

**Attention** : partout il faut utiliser la vraie IP du server dans les fichiers de config (localhost ne fonctionne pas...)

### Serveur de dialogue

- Décompresser l'archive
- Aller dans PyDial et suivre instructions README
	* Conseil : installer un virtualenv (virtualenv PyDial, puis source PyDial/bin/activate ensuite)
- Lancer python tests/test_Server.py
	* Ficher de config dans test/configs/*KUSTOM* : régler l'IP
	* googleSR.py : paramètre "fr-FR" l27, à remplacer par "en-EN" pour tester les domaines par défaut

==============

Pour tester le serveur :
curl -i -X POST -H 'Content-Type: application/json' -d '{"session": "9898"}' http://192.168.1.39:8082/newcall
curl -i -X POST -H 'Content-Type: application/json' -d '{"session": "9898","result":{"resultType":"Partial", "alts":[{"transcript":"i want an hotel", "confidence":1}]}}' http://192.168.1.39:8082/next
...
curl -i -X POST -H 'Content-Type: application/json' -d '{"session": "9898"}' http://192.168.1.39:8082/clean

==============

### NAO

- Démarrer Chorégraphe
- Ouvrir Projet NaoPyDialProject/NaoPyDial.pml
- Modifier boites PyDial et Recognition pour ajuster l'IP du serveur
- Connecter au NAO (soit filaire, soit wifi)
- Charger le projet sur le robot (F5)
- Tester


## Modifications PyDial

Les fichiers précédement rajoutés/modifiés sont :
	- SpeechRecognition a été ajoutée à requirements.txt

	- DialogueServer.py => fichier contenant le serveur Rest
	- googleSR.py => fait la connexion avec Google Speech
	- tests/test_Server.py => lance le serveur PyDial DialogueServer.py
	- utils/fixed_tokenize.py => le tokenizer, mais tolérant maintenant les accents (ASCII -> Unicode)

	Fichiers concernants la nouvelle base de données exemple McDonald's :
	- ontology/ontologies/KUSTOM-dbase.db
	- ontology/ontologies/KUSTOM-rules.json
	- semi/RegexSemI.py
	- semi/RegexSemI-KUSTOM.py
	- semo/templates/KUSTOMMessages.txt

	Certains autres fichiers ne sont pas listés, car moins importants.
	
Merci à N. Duret et L. Fournié, @CERI19, pour avoir fourni la base de de ce travail.

## Modifications PyDial 2019-2020 (Gontard Malvina et Casanova Delfeil)

Les fichiers modifiés sont :
	- SpeechRecognition a été ajoutée à requirements.txt

	- ./config/DialogueServer-Films.py => fichier de configuration du serveur 
	- tests/test_Server.py => lance le serveur PyDial DialogueServer.py
	- policy/HDCPolicy.py => Permet de mettre des exemples dans les Semo request()

	Fichiers concernants le nouveau modèle Films:
	- ontology/ontologies/Films-dbase.db
	- ontology/ontologies/Films-rules.json
	- semi/RegexSemI.py
	- semi/RegexSemI-Films.py
	- semo/templates/FilmsMessages.txt

