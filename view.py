from register_restful_api import app
from register_restful_api.API.view import register_user_api

app.register_blueprint(register_user_api)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
