from register_restful_api import user_collection


def insert_user_data(user_data):
    try:
        register_user = user_collection.insert_one(
            {
                'email': user_data.get('email'),
                'password': user_data.get('password'),
                'role': user_data.get('role'),
                'is_verified': user_data.get('is_verified')
            }
        )
        return register_user
    except:
        return {
            'Error': 'Unable to Register'
        }


def find_user_data(user_data):
    try:
        get_user_data = user_collection.find_one({'email': user_data}, {'_id': 0, 'update_time': 0})
        return get_user_data
    except:
        return {
            'Error': 'Not found'
        }


def update_verified_user(user_data):
    try:
        update_status = user_collection.update_one({'email': user_data}, {'$set': {'is_verified': True}})
        return update_status
    except:
        return {
            'ERROR': 'data is not valid'
        }
