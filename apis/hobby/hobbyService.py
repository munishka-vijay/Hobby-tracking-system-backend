from . import hobbyRepository
from utils.utils import *
from utils.errors import ERROR_MESSAGES

from datetime import datetime

def add_hobby(hobbyData):
    try:
        user_id = get_current_userid_from_token()
        start_date_obj = datetime.strptime(hobbyData['start_date'], "%Y-%m-%d").date()
        start_time_obj = datetime.strptime(hobbyData['start_time'], "%H:%M:%S").time()

        # Check if that hobby already exists 
        hobbyExists = hobbyRepository.find_hobby_by_name(hobbyData['name'])

        if hobbyExists['success'] == True:
            #Check if the hobby exists for that user
            for hobby in hobbyExists['data']:
                if hobby.user_id == user_id and hobby.start_time == start_time_obj:
                    return ERROR_MESSAGES["HOBBY_ALREADY_EXISTS"]

        addHobby = hobbyRepository.add_hobby(hobbyData['name'], hobbyData['tag_id'], user_id, start_date_obj, start_time_obj, hobbyData['duration'])

        return {
            'message': "New Hobby Added Successfully",
            'Hobby Name': addHobby.name,
            'Starting On': str(addHobby.start_date),
            'At Time': str(addHobby.start_time)
        }
    except Exception as err:
        return str(err)
    

def get_hobbies_for_user():
    try:
        user_id = get_current_userid_from_token()
        hobbies = hobbyRepository.get_hobbies_by_userid(user_id)
        hobbyList=[]
        if hobbies:
            for hobby in hobbies:
                hobbyList.append(
                    {
                        "Hobby Name" : hobby.name,
                        "Start Date" : str(hobby.start_date),
                        "Start Time" : str(hobby.start_time)
                    }
                )
            return hobbyList
        else:
            return ERROR_MESSAGES["HOBBY_NOT_FOUND"]
    except Exception as err:
        return str(err)
    
def get_all_hobbies():
    try:
        hobbies = hobbyRepository.get_all_hobbies()
        hobbyList=[]
        if hobbies:
            for hobby in hobbies:
                hobbyList.append(
                    {
                        "Hobby Name" : hobby.name,
                        "User ID" : hobby.user_id,
                        "Start Date" : str(hobby.start_date),
                        "Start Time" : str(hobby.start_time)
                    }
                )
            return hobbyList
        else:
            return ERROR_MESSAGES["HOBBY_NOT_FOUND"]
    except Exception as err:
        return str(err)
    
def update(id, hobbyData):
    try:
        user_id = get_current_userid_from_token()
        start_date_obj = datetime.strptime(hobbyData['start_date'], "%Y-%m-%d").date()
        start_time_obj = datetime.strptime(hobbyData['start_time'], "%H:%M:%S").time()
        
        # Check if hobby 
        hobbyExists = hobbyRepository.find_hobby_by_id(id)
        if hobbyExists['success'] is True:
            print(hobbyExists['data'])
            if hobbyExists['data'].user_id != user_id:
                return ERROR_MESSAGES["UNAUTHORIZED"]
        else:
            return ERROR_MESSAGES["HOBBY_NOT_FOUND"]

        hobby = hobbyRepository.update(id, hobbyData['name'], hobbyData['tag_id'], start_date_obj, start_time_obj, hobbyData['duration'])
        return {
            'message': "Hobby Updated Successfully",
            'Hobby Name': hobby.name,
            'Hobby Date': str(hobby.start_date),
            'Hobby Start Time': str(hobby.start_time)
        }
    except Exception as err:
        return str(err)
        

def delete(id):
    try:
        user_id = get_current_userid_from_token()
        hobby = hobbyRepository.find_hobby_by_id(id)

        if hobby['success'] is True:
            if hobby['data'].user_id != user_id:
                return ERROR_MESSAGES["UNAUTHORIZED"]
        else:
            return ERROR_MESSAGES["HOBBY_NOT_FOUND"]
        
        deletedHobby = hobbyRepository.delete(id)
        return {
            "Deleted Hobby Name" : deletedHobby,
            "message": "Hobby Deleted Successfully"
        }
    except Exception as err:
        return str(err)

    
