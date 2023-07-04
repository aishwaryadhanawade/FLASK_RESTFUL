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

def upadte_user_details(user_email,user_password):
    try:
        update_details=user_collection.update_one({'email':user_email},{'$set':{'password':user_password}})
        return update_details
    except:
        return {'ERROR':'Unable to update'}


def delete_user_data(user_email):
    try:
        delete_user=user_collection.delete_one({'email':user_email})
        return delete_user
    except:
        return {
            'ERROR':'unable to delete'
        }