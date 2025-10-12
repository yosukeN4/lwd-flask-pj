from flask import Flask, request
from flask import render_template

import boto3

from decimal import Decimal
from movies import Movies
import logging

import os

os.environ['AWS_DEFAULT_REGION'] = 'ap-northeast-1'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

# set global variable
table_name = "test_getstart"
dyn_resource = boto3.resource("dynamodb")
movies = Movies(dyn_resource)
movies_exists: bool = movies.exists(table_name)

@app.route('/')
def hello_world():
    return 'Hello, WorlDADA!'


@app.route('/movies', methods=["GET"])
def item_get(movies=movies):
    """get item
    param title-sortkey: str
    param year-hasykey: int
    return: code :int and items: dict
    """ 
    title:str = request.args.get('title')
    year:int = request.args.get('year', type=int)
    item:dict = movies.get_movie(title, year)
    logger.debug(f"year: {year}")
    logger.debug(f"title: {title}")

    return {"Code": 200, "items": item}

@app.route('/movies/add', methods=["POST"])
def item_add(movies=movies):
    """add item
    param title-sortkey: str
    param year-hasykey: int
    param plot : str
    param rating : str
    return: code :int and status: str
    """ 
    data = request.get_json()
    movies.add_movie(
        title  = data.get('title'),
        year   = data.get('year'),
        plot   = data.get('plot'),
        rating = data.get('rating')
    )

    return {"Code": 200, "status": "Movie added successfully."}

@app.route('/movies/delete', methods=["POST"])
def item_delete(movies=movies):
    """delete item
    param title-sortkey: str
    param year-hasykey: int
    return: code :int and status: str
    """ 
    data = request.get_json()
    movies.delete_movie(
        title  = data.get('title'),
        year   = data.get('year')
    )

    return {"Code": 200, "status": "Movie deleted successfully."}

@app.route('/movies/exists', methods=["GET"])
def movie_exists(movies=movies,table_name=table_name):
    movies_exists: bool = movies.exists(table_name)

    return {"Code": 200, "is_movies_exists": movies_exists}



@app.route('/healthcheck', methods=["GET"])
def healthcheck():
    return {"Code":200, "body": "Server is fine."}



@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)