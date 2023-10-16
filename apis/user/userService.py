from . import userRepository
from utils.utils import *

def user_signup(user_info):
    try:
        #Check if username is already taken/user already exists
        user = userRepository.find_user_by_username(user_info['username'])
        if user['success']==True:
            raise Exception("User already exists")
        
        # Get the role from user_info (default to 'user' if not provided)
        role = user_info.get('role', 'user')
        
        #Hash the password
        hashedPassword = create_hashed_password(user_info['password'])
        
        #Add new user to DB
        added_user = userRepository.add_user(user_info['username'], user_info['email'], user_info['phone'], hashedPassword, role)

        #Generate JWT Token
        token = generate_jwt_token(added_user.id, added_user.username)
        
        return {
            'id': added_user.id,
            'username': added_user.username,
            'token':token,
            'role':added_user.role
        }
    
    except Exception as err:
        raise Exception(str(err))
    

def user_login(userData):
    try:

        # Check if user exists
        userExists = userRepository.find_user_by_username(userData['username'])
        if not userExists['success']:
            raise Exception("User does not exist")
        
        # Check if password is correct
        isPasswordCorrect = check_password(userData['password'], userExists['data'].password)

        if not isPasswordCorrect:
            raise Exception("Incorrect Password")
        
        token = generate_jwt_token(userExists['data'].id, userExists['data'].username)

        return {
            'id': userExists['data'].id,
            'username': userExists['data'].username,
            'token':token,
            'role':userExists['data'].role
        }
    
    except Exception as err:
        raise Exception(str(err))


        
    

