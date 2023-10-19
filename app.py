from flask import Flask, request
from flask_mysqldb import MySQL
from sqlalchemy import text
from flask_jwt_extended import JWTManager, jwt_required
from flask_principal import Principal

from utils.config import Config
from utils.utils import *
from database import db
from apis.user.userRoutes import user_api
from apis.tag.tagRoutes import tag_api

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.register_blueprint(user_api)
    app.register_blueprint(tag_api)

    jwt = JWTManager(app)
    principal = Principal(app)

    return app

app=create_app()

db.init_app(app)

with app.app_context():
    db.create_all()



@app.route("/",methods=["GET"])
def greetings():
    return "Hi from Hobby Tracking System"

@app.route("/test-db")
def test_db():
    try:
        db.session.execute(text("SELECT 1"))
        return 'Successfully connected to MYSQL DB'
    except Exception as e:
        return f'Failed to connect to the DB - Error: {str(e)}'
    
@app.route("/get-current-user-role")
@jwt_required()
def get_user_role():
    try:
        return get_current_user_from_token()
    except Exception as e:
        return str(e)


if __name__=="__main__":
    app.run(debug=True) #We set debug=True so that everytime we make a change, our server restarts by itself
