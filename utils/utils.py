import bcrypt, jwt
from flask_bcrypt import check_password_hash
from datetime import datetime, timedelta
from .config import Config
from .errors import ERROR_MESSAGES


def create_hashed_password(password):
    # Salt is a random string used during hashing
    salt=bcrypt.gensalt()

    # Hash password using salt
    hashed_pwd = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed_pwd.decode("utf-8")

def generate_jwt_token(user_id, username):

    # Set expiry for jwt token

    expiration = datetime.utcnow() + timedelta(hours=Config.JWT_ACCESS_TOKEN_EXPIRES)
    expiration_timestamp = expiration.timestamp()
    #Create payload using useri, username and expiry
    payload = {
        'user_id': user_id,
        'username': username,
        'expiry':expiration_timestamp
    }

    # Generate the JWT token using the secret key from the Flask app configuration
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')

    return token

# To check if user has entered correct password
def check_password(password, hashedPassword):
    print(password, hashedPassword)
    return check_password_hash(hashedPassword, password)

# To check if JWT Token is valid
def check_jwt_token(token):
    payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
    expiry_timestamp = payload['expiry']
    expiry_datetime = datetime.fromtimestamp(expiry_timestamp)

    # Now, you can check if the token has expired
    if expiry_datetime < datetime.utcnow():
        # Token has expired
        return False

    # Token is valid
    return True

# def admin_required(fn):
#     @wraps(fn)
#     def decorated_function(*args, **kwargs):
#         if current_user.role != 'admin':
#             # If the user is not an admin, deny access
#             # abort(403)  # You can customize the error page for a forbidden request
#             raise Exception(ERROR_MESSAGES["UNAUTHORIZED"])
#         return fn(*args, **kwargs)
#     return decorated_function
