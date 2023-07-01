from Register_API import user_collection


def insert_user_data(user_data):
    try:
        register_user = user_collection.insert_one(
            {
                'email': user_data.get('email'),
                'password': user_data.get('password'),
                'role': 'Admin',
                'is_verified': False
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
