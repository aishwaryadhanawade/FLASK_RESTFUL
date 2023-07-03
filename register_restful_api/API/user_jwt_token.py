from register_restful_api.API.controller import *
from flask import Flask,request
import jwt

def authentication_token(func):
    def wapper_data(*args):
        bearer_token=request.headers.get('authorization')
        jwt_decoded_token=jwt.decode(bearer_token,'secret_key',algorithms='HS256')
        # token_data=jwt_decoded_token['data']['email']
        # print(token_data)
        return func(*args,jwt_decoded_token)
    return wapper_data


# def authorization_token(func):
#     def wapper_data(*args):
#         token_user=request.headers.get('')
#         return func(*args)
#     return wapper_data

