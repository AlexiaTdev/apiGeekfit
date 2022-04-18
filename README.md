# apiGeekfit

## dev
**virtual environnement**
https://docs.python.org/fr/3/library/venv.html
https://www.youtube.com/watch?v=mEUSNId1Hfc&ab_channel=ParwizForogh
https://www.youtube.com/watch?v=mEUSNId1Hfc&ab_channel=ParwizForogh
https://docs.google.com/spreadsheets/d/1OsP6hpFKBpuHRt95DqZw1-cb5kK-ZYw2tDmvgXyCYA8/edit#gid=25797257
https://github.com/dsznajder/vscode-react-javascript-snippets/blob/HEAD/docs/Snippets.md                   snippets rfe rfc

projet :
api en python
react front

**Step installation**
**Faire tourner le projet pour la première fois**
j'ouvre un terminal, je me mets là où je veux placer mon dossier avec "cd /path/...."
"git init"
"git remote add origin pathACollerDepuisGitHub"
"git pull origin main"
-> tu es maintenant relié au repo

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

# installer son venv avec le requirements.txt
dans le terminal depuis le dossier /api
python -m pip install -r requirements.txt
-> configure le venv

**Step développement**
**MANIP TUTO FLASK python react**

###faire fonctioner son projet :
#activer /désactiver venv depuis powershell
Activer
PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> .\\api\venv\Scripts\Activate.ps1
ou encore PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> .\\app\venv\Scripts\Activate.ps1
Desactiver
(venv) PS C:\Users\teiss\Documents\EPSI\I1\GEEKFIT> deactivate

**Run API**
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

**Creer db**
(Pour le moment chacun créé sa bd chez lui lorsqu'il bosse sur le projet
#créer la db depuis flask
dans /api
python (ouvre un python terminal)
from app import db
db.create_all()
result : c'est maintenant linked et se met à jour automatiquement


**GITFLOW (PROCESS DEV SUR GIT)**
!!!AVANT DE COMMENCER TON DEV!!!!
git checkout main
-> doit renvoyer "Your branch is up to date with 'origin/main'.". S'il n'est pas à jour, faire un "git pull origin main"
git branch nomDeTaBranche   (ex : ID3_page_connexion_detail -> IDnuméro de la user story et titre avec _)
git checkout nopmDeTaBranche (ex : ID3_page_connexion_detail)
!!!!!!(tu dev)!!!!!
git add *
git commit -m "nomducommi"
git push -u origin






parametrage flask
lancer avec
flask run --host=0.0.0.0
sur mon ip dans app.py
http://192.168.2.209:19000/
dans le fetch côté réact

https://reactnavigation.org/docs/nesting-navigators

Configuration d'alexia seulement :
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





**ce que tu fais quand tu créé le projet**

#creer le projet
cd app
expo init nomDuProjet



créer un venv depuis cmd
C:\>C:\Python39\python -m venv C:/Users/teiss/Documents/EPSI\I1/GEEKFIT/app/venv 


