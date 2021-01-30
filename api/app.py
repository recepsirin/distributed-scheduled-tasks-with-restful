from flask import Flask
from flask_restful import Api
from models.players import initialize_db
from routing.routes import initialize_routes
from helpers.yml_parser import parser

app = Flask(__name__)
api = Api(app)

app.config['TESTING'] = parser()['TESTING']
app.config['DEBUG'] = parser()['DEBUG']

app.config['MONGODB_SETTINGS'] = {
    'host': parser()['database']['mongo']['dsn']
}


def initialize():
    initialize_db(app)
    initialize_routes(api)


def start_app():
    initialize()
    app.run()


if __name__ == '__main__':
    start_app()
