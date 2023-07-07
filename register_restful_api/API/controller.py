from register_restful_api import user_collection


def insert_user_data(user_data):
    try:
        register_user = user_collection.insert_one(
            {
                'email': user_data.get('email'),
                'password': user_data.get('password'),
                'role': user_data.get('role'),
                'is_verified': user_data.get('is_verified'),
                'is_deleted': False
            }
        )
        result = True if register_user.acknowledged else False
        return result
    except:
        return {
            'error': 'Unable to Register'
        }


def find_user_data(user_data):
    try:
        get_user_data = user_collection.find_one({'email': user_data})
        if get_user_data:
            return True
        else:
            return False
    except Exception as e:
        import traceback
        print(traceback.print_exc())
        return {
            'error': 'Not found'
        }

# obj = {"email":"pamit1687@gmail.com"}
# print(find_user_data(obj))s

def update_verified_user(user_data):
    try:
        update_status = user_collection.update_one({'email': user_data}, {'$set': {'is_verified': True}})
        return update_status
    except:
        return {
            'error': 'data is not valid'
        }


def update_user_details(user_email, user_password):
    try:
        update_details = user_collection.update_one({'email': user_email}, {'$set': {'password': user_password}})
        return update_details
    except:
        return {'error': 'Unable to update'}


def delete_user_data(user_email):
    try:
        delete_user = user_collection.update_one({'email': user_email}, {'$set': {'is_deleted': True,'is_verified':False}})
        return delete_user
    except:
        return {
            'error': 'unable to delete'
        }
