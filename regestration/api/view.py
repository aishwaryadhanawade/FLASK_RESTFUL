from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from regestration.api.controller import *
from flask_jwt_extended import create_access_token, jwt_required
from regestration import JWT_ACCESS_TOKEN_TIMEDELTA

reg = Blueprint('reg', __name__)
reg_api = Api(reg)


class Register(Resource):
    def post(self):
        try:
            data = request.get_json()

            username = data.get('username', 'NA')
            password = data.get('password', 'NA')

            existing_user = get_user_info(username)
            print(existing_user)

            if existing_user:

                return jsonify({'Response': 'user is already exist'})
            else:
                user_data = {'username': username, 'password': password}
                data = insert_data(user_data)
                if data:
                    return jsonify({'Inserted': 'User is Register Successful'})

        except:
            return jsonify({'Response': 'Data is not present'})

    def get(self):
        try:
            r = get_data()
            user = []
            for i in r:
                user.append(i)
            return user
        except:
            return jsonify({'Error': 'unable to access data'})


class Login(Resource):
    def post(self):
        login_data = request.get_json()

        passw = login_data.get('password')

        username = get_user_info(login_data['username'])
        if username:
            if passw == username['password']:
                access_for_login = create_access_token(identity=login_data['username'],expires_delta=JWT_ACCESS_TOKEN_TIMEDELTA)
                return jsonify({'Access_token': access_for_login})
            else:
                return jsonify({'Error': 'Incorrect password'})
        else:
            return jsonify({'Error': 'invalid credentials'})


class Delete_user(Resource):
    @jwt_required()
    def post(self):
        try:
            user_data = request.get_json()

            del_user = get_user_info(user_data['username'])
            if del_user:
                delete_user(del_user)
            return jsonify({'Response': 'User deleted'})
        except:
            return jsonify({'ERROR': 'user is not present'})


class Update_user(Resource):
    def post(self):
        try:
            user_data = request.get_json()
            up_user = get_user_info(user_data['username'])
            update_info = user_data['password']

            if up_user:
                Update_user_data(up_user, update_info)
            return jsonify({'Response': 'user updated'})

        except:

            return jsonify({'ERROR': 'Data is invalid'})


reg_api.add_resource(Register, '/register')
reg_api.add_resource(Login, '/login')
reg_api.add_resource(Delete_user, '/delete')
reg_api.add_resource(Update_user, '/update')
