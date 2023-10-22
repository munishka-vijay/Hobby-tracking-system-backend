from flask import Blueprint,request, jsonify
from flask_jwt_extended import jwt_required

from . import hobbyService

hobby_api = Blueprint('hobby', __name__, url_prefix='/hobby')

#to create a hobby
@hobby_api.route('/', methods=['POST'])
@jwt_required()
def add_hobby():
    try:
        hobbyData = request.get_json()
        hobbyAdded = hobbyService.add_hobby(hobbyData)
        return jsonify(hobbyAdded)
    except Exception as err:
        return str(err)

#to get all hobbies    
@hobby_api.route('/', methods=['GET'])
@jwt_required()
def get_hobbies_for_user():
    try:
        hobbies = hobbyService.get_hobbies_for_user()
        return jsonify(hobbies)
    except Exception as err:
        return str(err)



