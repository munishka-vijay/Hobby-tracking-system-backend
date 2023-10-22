from database import db
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
    
def find_hobby_by_id(id):
    try:
        hobbies = Hobby.query.filter_by(id = id).first()
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
    print(userid)
    try:
        hobbies = Hobby.query.filter_by(user_id=userid).all()
        return hobbies
    except Exception as err:
        return str(err)

def get_all_hobbies():
    try:
        hobbies = Hobby.query.all()
        return hobbies
    except Exception as err:
        return str(err)

def update(id, name, tag_id, start_date_obj, start_time_obj, duration):
    try:
        hobby = Hobby.query.filter_by(id = id).first()
        hobby.name = name
        hobby.tag_id = tag_id
        hobby.start_date = start_date_obj
        hobby.start_time = start_time_obj
        hobby.duration = duration
        hobby.save()
        return hobby
    except Exception as err:
        return str(err)

def delete(id):
    try:
        hobby = Hobby.query.filter_by(id = id).first()
        hobbyName = hobby.name 
        db.session.delete(hobby)
        db.session.commit()
        return hobbyName
    except Exception as err:
        return str(err)

