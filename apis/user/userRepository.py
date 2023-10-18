from .userModel import User
from utils.errors import ERROR_MESSAGES

def add_user(username, email, phone, password, role):
    try:
        new_user = User(username=username, email= email, phone=phone, password=password, role=role)
        new_user.save()
        return new_user
    except Exception as err:
        return str(err)
    
def find_user_by_username(username):
    try:
        user = User.query.filter_by(username=username).first()
        if user:
            return {
                'success': True,
                'data': user,
            }

        raise Exception("USER_NOT_FOUND")
    except Exception as err:
        return {
            'success': False,
            'error': str(err),
        }

# To get role of user    
def get_user_role(user_id):

    # Getting role of the user from user_id
    user = User.query.filter_by(id=user_id).first()

    if user:
        return user.role
    else:
        # Handle the case where the user doesn't exist
        raise Exception(ERROR_MESSAGES["USER_NOT_FOUND"])

# To check if user is admin    
def is_admin(user_id):
    # Assuming you have a function to get the user's role from the database
    user_role = get_user_role(user_id)
    return user_role == 'admin'

        

