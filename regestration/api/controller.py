from regestration import coll


def get_user_info(user):
    print(user)
    try:
        data = coll.find_one({'username': user}, {"_id": 0, "update_time": 0})
        # print(data)
        return data
    except:
        return "Check Your username"


def insert_data(user_info):
    print(user_info)
    try:
        data = coll.insert_one(user_info)
        return data
    except:
        return "Insertion is not possible"


def get_data():
    try:
        data = list(coll.find({}, {"_id": 0, "update_time": 0}))
        return data
    except:
        return "Error"


def delete_user(user_info):
    try:
        data = coll.delete_one(user_info)
        return data
    except:
        return "User information is not valid"


def Update_user_data(user_info, updated_data):
    try:
        data = coll.update_one({'username': user_info['username']},
                               {'$set': {'password': updated_data}})
        return data
    except:
        return "Update is not possible"
