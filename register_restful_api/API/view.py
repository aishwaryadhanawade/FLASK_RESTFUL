from register_restful_api import api, app
from flask_restful import Resource, Api
from flask import request, jsonify, Blueprint
from register_restful_api.API.controller import *
import os
import smtplib
from datetime import datetime, timedelta
import jwt
from register_restful_api.API.user_jwt_token import authentication_token
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, get_jwt_identity
from register_restful_api import JWT_ACCESS_TOKEN_TIMEDELTA

register_user_api = Blueprint('register_user_api', __name__)
register_api = Api(register_user_api)


class RegisterUser(Resource):
    def post(self):
        try:
            user_details = request.get_json()
            email = user_details.get('email')
            password = user_details.get('password')
            role = 'Admin'
            is_verified = False
            token_expiry_time = datetime.now() + timedelta(minutes=15)
            token_expiry_time_epoch = int(token_expiry_time.timestamp())

            existing_email = find_user_data(email)
            if existing_email:
                return jsonify({'Response': 'Email is already Register'})
            try:
                encoded_data = {
                    'data': {'email': email, 'role': role, 'is_verified': is_verified},
                    'exp': token_expiry_time_epoch
                }
                user_auth_token = jwt.encode(encoded_data, 'secret_key', algorithm='HS256')

                sender_mail = os.environ.get('sender_gmail')
                sender_password = os.environ.get('app_password')
                smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
                smtpobj.starttls()
                smtpobj.login(sender_mail, sender_password)
                smtpobj.sendmail(sender_mail, email, user_auth_token)

                register_user_data = {'email': email, 'password': password, 'role': role, 'is_verified': is_verified}
                insert_user_data(register_user_data)
                return jsonify({'Response': 'mail send'})

            except:
                return jsonify({'ERROR': 'unable to send email'})
        except:
            return jsonify({'Error': 'Please enter valid data'})


class Verify_user(Resource):
    @authentication_token
    def post(self, data):
        try:
            user_email_from_token = data['data']['email']
            authenticate = find_user_data(user_email_from_token)
            if authenticate:
                update_status = update_verified_user(user_email_from_token)
                if update_status:
                    return jsonify({'Success': 'user is verified'})
                else:
                    return jsonify({'Error': 'unable to verify user'})
        except:
            return jsonify({'ERROR': 'User data is invalid'})


class Login_user(Resource):
    def post(self):
        try:
            user_login_email = request.json.get('email')
            user_login_password = request.json.get('password')
            user_data = find_user_data(user_login_email)
            # print(user_data)

            if user_data:
                if user_data['password'] == user_login_password and user_data['is_verified'] == True:
                    user_access_token = create_access_token(identity=user_login_email,
                                                            expires_delta=JWT_ACCESS_TOKEN_TIMEDELTA)
                    user_refresh_token = create_refresh_token(identity=user_login_email)
                    return jsonify({'Response': 'user login successfully',
                                    'access_token': user_access_token,
                                    'refresh_token': user_refresh_token
                                    })
                else:
                    return jsonify({'Error': 'Data is not verified'})
            else:
                return jsonify({'Error': 'user data is invalid'})
        except:
            return jsonify({'ERROR': 'user not found'})


class Update_user(Resource):
    @jwt_required()
    def post(self):

        try:
            update_user_data = get_jwt_identity()
            update_user_password = request.json.get('password')
            current_user_details = find_user_data(update_user_data)
            if current_user_details:
                if current_user_details['role'] == 'Admin':
                    upadte_user_details(update_user_data, update_user_password)
                    return jsonify({'current_user': 'user data updated'})
                else:
                    return jsonify({'Error': 'Not authorized user for update'})
            else:
                return jsonify({'ERROR': 'user is not valid'})
        except:
            return jsonify({'ERROR': 'Data is invalid'})


class Delete_user(Resource):
    @jwt_required()
    def post(self):
        try:
            delete_user = get_jwt_identity()
            find_user_availability = find_user_data(delete_user)
            if find_user_availability:
                if find_user_availability['role'] == 'Admin':
                    delete_user_data(delete_user)
                    return jsonify({'Response': 'user is deleted'})
                return jsonify({'Error': 'Not authorized user for delete'})
            return jsonify({'ERROR': 'user is not register'})
        except:
            return jsonify({'ERROR': 'user is not valid'})


register_api.add_resource(RegisterUser, '/register')
register_api.add_resource(Verify_user, '/verify')
register_api.add_resource(Login_user, '/login')
register_api.add_resource(Update_user, '/update')
register_api.add_resource(Delete_user, '/delete')
