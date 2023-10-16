from flask import Flask
from flask_mysqldb import MySQL
from sqlalchemy import text

from utils.config import Config
from database import db
from apis.user.userRoutes import user_api

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.register_blueprint(user_api)

    return app

app=create_app()

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/",methods=["GET"])
def greetings():
    return "Hi from Flask"

@app.route("/test-db")
def test_db():
    try:
        db.session.execute(text("SELECT 1"))
        return 'Successfully connected to MYSQL DB'
    except Exception as e:
        return f'Failed to connect to the DB - Error: {str(e)}'


if __name__=="__main__":
    app.run(debug=True) #We set debug=True so that everytime we make a change, our server restarts by itself