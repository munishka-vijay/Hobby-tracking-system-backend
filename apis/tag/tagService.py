import re
from . import tagRepository
from utils.errors import ERROR_MESSAGES

def add_new_tag(name):
    try:
        
        #Check if Tag contains only alphabets
        if not re.match("^[a-zA-Z ]+$", name):
            raise Exception(ERROR_MESSAGES["INVALID_TAG"])
        
        #Check if tag starts with Uppercase Letter
        if not name[0].isupper():
            raise Exception(ERROR_MESSAGES["INVALID_TAG_UPPERCASE_ERROR"]) 
        
        newTag = tagRepository.save_new_tag(name)

        return {
            'message': 'New Tag Added Successfully',
            'Tag Name': newTag.name
        }
    
    except Exception as err:
        return str(err)
    
def get_all_tags():
    try:
        tags = tagRepository.get_all_tags()

        # Transform the list of tag objects into a list of dictionaries
        tags_list = [{
            'id': tag.id,
            'name': tag.name,
        } for tag in tags]

        return tags_list
    except Exception as err:
        raise Exception(str(err))
    
def delete_tag_by_id(id):
    try:
        result = tagRepository.delete_tag_by_id(id)

        if result['success']:
            return {
                'success': True,
                'message': 'Tag deleted successfully'
            }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while deleting the tag')
            }
    except Exception as err:
        raise Exception(str(err))
    
def update_tag_by_id(tagId,tagName):
    try:
        result = tagRepository.update_tag_by_id(tagId , tagName)

        if result['success']:
            return {
                'success': True,
                'message': 'Tag updated successfully'
            }
        else:
            return {
                'success': False,
                'error': result.get('error', 'An error occurred while update the tag')
            }
    except Exception as err:
        raise Exception(str(err))