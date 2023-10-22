

from .hobbyModel import Hobby
from utils.errors import ERROR_MESSAGES

def find_hobby_by_name(name):
    try:
        hobbies = Hobby.query.filter_by(name = name)
        if hobbies:
            return {
                'success' : True,
                'data' : hobbies
            }
        else:
            return {
                'success' : False
            }

    except Exception as err:
        return str(err)
    
def add_hobby(name, tag_id, user_id, start_date_obj, start_time_obj, duration):
    try:

        newHobby = Hobby(
            name=name,
            tag_id=tag_id,
            user_id=user_id,
            start_date=start_date_obj,
            start_time=start_time_obj,
            duration=duration
        )
        newHobby.save()
        return newHobby
    except Exception as err:
        print("Adding new Hobby error: ", str(err))
        raise Exception(ERROR_MESSAGES["SOMETHING_WENT_WRONG"])
    
def get_hobbies_by_userid(userid):
    try:
        print(userid)
        hobbies = Hobby.query.filter_by(user_id=userid).all()
        return hobbies
    except Exception as err:
        return str(err)