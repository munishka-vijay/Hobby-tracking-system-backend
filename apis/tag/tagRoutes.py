from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from . import tagService

tag_api = Blueprint('tag', __name__, url_prefix='/tag')

# To add a tag
@tag_api.route('/addtag', methods=['POST'])
@jwt_required()
def add_tag():
    try:

        tagName=request.get_json()
        addedTag = tagService.add_new_tag(tagName['name'])
        return jsonify(addedTag)
    
    except Exception as err:
        return str(err)
    
# To get all tags    
@tag_api.route('/getalltags', methods=['GET'])
@jwt_required()
def get_all_tags():
    try:
        tags = tagService.get_all_tags()
        return jsonify(tags)
    except Exception as err:
        return str(err)
    
# To delete tag by id
@tag_api.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    try:
        tagData = tagService.delete_tag_by_id(id)

        if 'error' in tagData:
            error = tagData['error']
            return jsonify(error), 400

        return jsonify(tagData), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500
    
# To update tag by id
@tag_api.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    try:
        tagName=request.get_json()
        tagData = tagService.update_tag_by_id(id, tagName['name'])

        if 'error' in tagData:
            error = tagData['error']
            return jsonify(error), 400

        return jsonify(tagData), 201

    except Exception as err:
        return jsonify({'message': str(err)}), 500
    

