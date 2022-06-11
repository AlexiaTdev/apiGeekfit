import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
###################
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow


# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mysql+mysqldb://flaskapi2:api2022!@localhost:3309/flask")

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    firstname = sqlalchemy.Column(sqlalchemy.String(length=100))
    lastname = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

########################
app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#######################
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text(100))
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
#################################################


@app.route('/', methods = ['GET'])
def get_connection_basis():
    return jsonify({"hello":"hello"})


@app.route('/get', methods = ['GET'])
def get_articles():
    all_articles = session.query(Articles).all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)

@app.route('/get/<id>/', methods = ['GET'])
def post_details(id):
    article = session.query(Articles).get(id)
    return article_schema.jsonify(article)

@app.route('/add', methods = ['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    session.add(articles)
    session.commit()
    return article_schema.jsonify(articles)

@app.route('/update/<id>/', methods = ['PUT'])
def update_article(id):
    article = session.query(Articles).get(id)
    title = request.json['title']
    body = request.json['body']
    article.title = title
    article.body = body
    session.commit()
    return article_schema.jsonify(article)


@app.route('/delete/<id>/', methods = ['DELETE'])
def article_delete(id):
    article = session.query(Articles).get(id)
    session.delete(article)
    session.commit()
    return article_schema.jsonify(article)
