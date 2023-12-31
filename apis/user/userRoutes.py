from flask import Blueprint, request, jsonify

from . import userService

user_api = Blueprint('user', __name__, url_prefix='/user')

@user_api.route('/signup',methods=['POST'])
def signup():
    try:
        user_data = request.get_json()

        user_added = userService.user_signup(user_data)
        if 'error' in user_added:
            error = user_added['error']
            print("Error",error)
            return jsonify(error), 400

        return jsonify(user_added), 201

    except Exception as err:
        return str(err)
    
@user_api.route('/login', methods=['POST'])
def login():
    try:
        userData=request.get_json()
        userLogin=userService.user_login(userData)

        if 'error' in userLogin:
            error = userLogin['error']
            print("Error",error)
            return jsonify(error), 400

        return jsonify(userLogin), 201

    except Exception as err:
        return str(err)
    
