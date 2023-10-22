from database import db
from .tagModel import Tag
from utils.errors import ERROR_MESSAGES

def save_new_tag(name):
    try:
        newTag = Tag(name=name)
        newTag.save()
        return newTag
    except Exception as err:
        print("ADDING new tag error", str(err))
        return ERROR_MESSAGES["SOMETHING_WENT_WRONG"]

def get_all_tags():
    try:
        tags = Tag.query.order_by(Tag.id).all()
        if tags:
            return tags  # Return the list of Theatre objects
        raise Exception(ERROR_MESSAGES["TAG_NOT_FOUND"])
    except Exception as err:
        raise Exception(str(err))
    
#delete tag
def delete_tag_by_id(id):
    try:
        # Check if the theatre with the given ID exists
        tag_to_delete = Tag.query.get(id)
        
        if tag_to_delete:
            db.session.delete(tag_to_delete)
            db.session.commit()
            return {'success': True, 'message': 'Tag deleted successfully'}
        else:
            raise Exception(ERROR_MESSAGES["TAG_NOT_FOUND"])
    except Exception as err:
        return {'success': False, 'error': str(err)}
    

# Update tag by Id
def update_tag_by_id(id, name):
    try:
        # Check if the tag with the given ID exists
        tag_to_update = Tag.query.get(id)
        
        if tag_to_update:
            # Update the tag name
            tag_to_update.name = name
            db.session.commit()

            return {
                'success': True,
                'message': 'Tag updated successfully'
            }
        
        else:
            raise Exception(ERROR_MESSAGES["TAG_NOT_FOUND"])
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }


