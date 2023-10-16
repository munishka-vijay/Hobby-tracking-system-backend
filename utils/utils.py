import bcrypt, jwt
from flask_bcrypt import check_password_hash
from datetime import datetime, timedelta
from .config import Config


def create_hashed_password(password):
    # Salt is a random string used during hashing
    salt=bcrypt.gensalt()

    # Hash password using salt
    hashed_pwd = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed_pwd.decode("utf-8")

def generate_jwt_token(user_id, username):

    # Set expiry for jwt token
    expiry=datetime.utcnow() + timedelta(hours=Config.JWT_ACCESS_TOKEN_EXPIRES)

    # expiration = datetime.utcnow() + timedelta(hours=Config.JWT_ACCESS_TOKEN_EXPIRES)

    #Create payload using useri, username and expiry
    payload = {
        'user_id': user_id,
        'username': username,
    }

    # Generate the JWT token using the secret key from the Flask app configuration
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')

    return token

def check_password(password, hashedPassword):
    print(password, hashedPassword)
    return check_password_hash(hashedPassword, password)
