from database import db
from .userModel import User

def add_user(username, email, phone, password, role):
    try:
        new_user = User(username=username, email= email, phone=phone, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
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

        

