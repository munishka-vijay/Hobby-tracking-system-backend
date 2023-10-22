from flask import Blueprint,request, jsonify
from flask_jwt_extended import jwt_required

from . import hobbyService
from utils.utils import *

hobby_api = Blueprint('hobby', __name__, url_prefix='/hobby')

# to create a hobby
@hobby_api.route('/', methods=['POST'])
@jwt_required()
def add_hobby():
    try:
        hobbyData = request.get_json()
        hobbyAdded = hobbyService.add_hobby(hobbyData)
        return jsonify(hobbyAdded)
    except Exception as err:
        return str(err)

# to get all hobbies per user id   
@hobby_api.route('/', methods=['GET'])
@jwt_required()
def get_hobbies_for_user():
    try:
        hobbies = hobbyService.get_hobbies_for_user()
        return jsonify(hobbies)
    except Exception as err:
        return str(err)
    
# to get all hobbies
@hobby_api.route('/getall', methods=['GET'])
@jwt_required()
@admin_required
def get_all_hobbies():
    try:
        hobbies = hobbyService.get_all_hobbies()
        return jsonify(hobbies)
    except Exception as err:
        return str(err)
    
# to update hobby
@hobby_api.route("/<int:id>", methods=['PUT'])
@jwt_required()
def update_hobby(id):
    try:
        hobbyData = request.get_json()
        hobby = hobbyService.update(id, hobbyData)
        return jsonify(hobby)
    except Exception as err:
        return str(err)

# to delete hobby
@hobby_api.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    try:
        hobby=hobbyService.delete(id)
        return jsonify(hobby)
    except Exception as err:
        return str(err)


