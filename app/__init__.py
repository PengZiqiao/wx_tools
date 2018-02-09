from flask import Flask
from flask_restful import Api

from app.exts import db
from app.restful_api import Login, Friends, SaveFriends, SetRemark
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # database
    db.init_app(app)

    # restful
    api = Api(app)
    api.add_resource(Login, '/login')
    api.add_resource(Friends, '/friends')
    api.add_resource(SaveFriends, '/savefriends')
    api.add_resource(SetRemark, '/setremark')

    return app


app = create_app()
