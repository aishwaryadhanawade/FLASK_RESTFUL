from Register_API import api, app
from flask_restful import Resource
from flask import request, jsonify, Blueprint
from Register_API.API.cotroller import *
import smtplib

register_user_api = Blueprint('register_user_api', __name__)


class RegisterUser(Resource):
    def post(self):
        try:
            user_details = request.get_json()
            email = user_details.get('email')
            password = user_details.get('password')

            existing_email = find_user_data(email)
            if existing_email:
                return jsonify({'Response': 'Email is already Register'})
            try:
                smtpobj = smtplib.SMTP('localhost')
                smtpobj.sendmail('aishwaryadhanawade612@gmail.com', email, 'http//login.com')
                register_user_data = {'email': email, 'password': password}
                insert_user_data(register_user_data)

            except:
                return jsonify({'ERROR': 'unable to send email'})




        except:
            return jsonify({'Error': 'Please enter valid data'})
