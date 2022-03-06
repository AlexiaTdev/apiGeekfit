# apiGeekfit

## dev
**virtual environnement**
https://docs.python.org/fr/3/library/venv.html




https://www.youtube.com/watch?v=mEUSNId1Hfc&ab_channel=ParwizForogh
https://www.youtube.com/watch?v=mEUSNId1Hfc&ab_channel=ParwizForogh


https://docs.google.com/spreadsheets/d/1OsP6hpFKBpuHRt95DqZw1-cb5kK-ZYw2tDmvgXyCYA8/edit#gid=25797257
https://github.com/dsznajder/vscode-react-javascript-snippets/blob/HEAD/docs/Snippets.md                   snippets rfe rfc



MANIP TUTO FLASK python react

api
react front

##imports :
--partie back flask
pip install Flask
	web application framework
pip install Flask-SQLAlchemy
	extension de flask with usefull default
	https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
pip install mysqlclient (peut etre postgres, etc)
pip install flask-marshamallow
	deserialization lib including url end hperlinks HATEOAS api
pip install marshmallow-sqlalchemy

--partie front react native
npm install -g expo-cli
npm install @react-native-paper                   ---pour les boutons
npm install @react-navigation/native              ---pour les route


###faire fonctioner son projet :

créer un venv depuis cmd
C:\>C:\Python39\python -m venv C:/Users/teiss/Documents/EPSI\I1/GEEKFIT/app/venv 

#activer /désactiver venv depuis powershell
PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> .\\api\venv\Scripts\Activate.ps1
ou encore PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> .\\app\venv\Scripts\Activate.ps1
(venv) PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> 
(venv) PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> deactivate
PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> 


#run en debug true depuis vscode
f5 
flask
chemin du fichier, entrer
résultat : http://127.0.0.1:5000/  & on voit hello world
OU on va sur la page app et on execute "démarrage du debuggage"

#ouvrir postman
collection GeekFit créée


#lancer phpMyAdmin local
ouvrir wamp
démarrer le service mariadb port 3306 et enlever mysql de mes deux
http://localhost/phpmyadmin/index.php?route=/&route=%2F
id root mdp riendutout


#créer la db depuis flask
dans /api
python (ouvre un python terminal)
from app import db
db.create_all()
result : c'est maintenant linked et se met à jour automatiquement

#creer le projet
cd app
expo init nomDuProjet




parametrage flask
lancer avec
flask run --host=0.0.0.0
sur mon ip dans app.py
http://192.168.2.209:19000/
dans le fetch côté réact

https://reactnavigation.org/docs/nesting-navigators

j'en suis au step15 creation branche step15 react project poc

**** il existe deux github
git push -u poc    ---->github poc
git push -u origin ---->github GEEKFIT




pour faire fonctionner en développement
(venv) PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT\api> flask run --host=0.0.0.0
(venv) PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT\api> python
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32  
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
>>> db.create_all()



GITFLOW (PROCESS DEV SUR GIT)
depuis le main
git branch nopmDeTaBranche
git checkout nopmDeTaBranche
(tu dev)
git add *
git commit -m "nomducommi"
git push -u origin
