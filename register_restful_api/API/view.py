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
from passlib.hash import sha256_crypt
# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

register_user_api = Blueprint('register_user_api', __name__)
register_api = Api(register_user_api)


class Default(Resource):
    def get(self):
        return "Hello"

class RegisterUser(Resource):
    def post(self):
        try:
            # user_details = request.get_json()
            email = request.json.get('email')
            password = request.json.get('password')
            print(email,password)
            role = 'Admin'
            is_verified = False
            token_expiry_time = datetime.now() + timedelta(minutes=15)
            token_expiry_time_epoch = int(token_expiry_time.timestamp())

            encrypt_password = sha256_crypt.encrypt(str(password))
            print(encrypt_password)

            existing_email = find_user_data(email)
            print(existing_email)
            if existing_email:
                return jsonify({'response': 'Email is already Register'})

            try:
                encoded_data = {
                    'data': {'email': email, 'role': role, 'is_verified': is_verified},
                    'exp': token_expiry_time_epoch
                }
                user_auth_token = jwt.encode(encoded_data, 'secret', algorithm='HS256')

                msg_token = f'''<html>
                                    <body>
                                        <p>To verify your email</p>
                                        <b><a href="http://127.0.0.1:5000//v1/api/verify?token={user_auth_token}">Click Here</a></b>
                                    </body>
                                </html>'''

                sender_mail = os.environ.get('sender_gmail')
                sender_password = os.environ.get('app_password')
                # sender_mail = "aishwaryadhanawade612@gmail.com"
                #
                # sender_password = "igxnzbkbjtnctwio"

                message = MIMEMultipart("alternative")
                message['Subject'] = "Verification Email"
                message['From'] = sender_mail
                message['To'] = email

                message_link = MIMEText(msg_token, 'html')
                message.attach(message_link)

                smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
                smtpobj.starttls()
                smtpobj.login(sender_mail, sender_password)
                smtpobj.sendmail(sender_mail, email, message.as_string())

                register_user_data = {'email': email,
                                      'password': password,
                                      'role': role,
                                      'is_verified': is_verified}
                insert_user_data(register_user_data)
                return jsonify({'response': 'mail send'})

            except Exception as e:
                import traceback
                print(traceback.print_exc())
                return jsonify({'error': str(e)})
        except Exception as e:
            return jsonify({'error': str(e)})


class Verify_user(Resource):
    @authentication_token
    def get(self, data):
        try:
            user_email_from_token = data['data']['email']
            authenticate = find_user_data(user_email_from_token)
            if authenticate:
                update_status = update_verified_user(user_email_from_token)
                if update_status:
                    return jsonify({'success': 'user is verified'})
                else:
                    return jsonify({'error': 'unable to verify user'})
        except:
            return jsonify({'error': 'User data is invalid'})


class Login_user(Resource):
    def post(self):
        try:
            user_login_email = request.json.get('email')
            user_login_password = request.json.get('password')
            user_data = find_user_data(user_login_email)
            # print(user_data)

            if user_data:
                if sha256_crypt.verify(str(user_login_password), user_data['password']) and user_data['is_verified'] == True and user_data['is_deleted'] == False:
                    user_access_token = create_access_token(identity=user_login_email,
                                                            expires_delta=JWT_ACCESS_TOKEN_TIMEDELTA)
                    user_refresh_token = create_refresh_token(identity=user_login_email)
                    return jsonify({'response': 'user login successfully',
                                    'access_token': user_access_token,
                                    'refresh_token': user_refresh_token
                                    })
                else:
                    return jsonify({'error': 'Data is not verified'})
            else:
                return jsonify({'error': 'user data is invalid'})
        except:
            return jsonify({'error': 'user not found'})


class Update_user(Resource):
    @jwt_required()
    def post(self):

        try:
            update_user_data = get_jwt_identity()
            update_user_password = request.json.get('password')
            current_user_details = find_user_data(update_user_data)
            encrypt_password = sha256_crypt.encrypt(str(update_user_password))
            if current_user_details:
                if current_user_details['role'] == 'Admin':
                    update_user_details(update_user_data, encrypt_password)
                    return jsonify({'current_user': 'user data updated'})
                else:
                    return jsonify({'error': 'Not authorized user for update'})
            else:
                return jsonify({'error': 'user is not valid'})
        except:
            return jsonify({'error': 'Data is invalid'})


class Delete_user(Resource):
    @jwt_required()
    def post(self):
        try:
            delete_user = get_jwt_identity()
            find_user_availability = find_user_data(delete_user)
            if find_user_availability:
                if find_user_availability['role'] == 'Admin':
                    delete_user_data(delete_user)
                    return jsonify({'response': 'user is deleted'})
                return jsonify({'error': 'Not authorized user for delete'})
            return jsonify({'error': 'user is not register'})
        except:
            return jsonify({'error': 'user is not valid'})


register_api.add_resource(Default, '/')
register_api.add_resource(RegisterUser, '/v1/api/register')
register_api.add_resource(Verify_user, '/v1/api/verify')
register_api.add_resource(Login_user, '/v1/api/login')
register_api.add_resource(Update_user, '/v1/api/update')
register_api.add_resource(Delete_user, '/v1/api/delete')
