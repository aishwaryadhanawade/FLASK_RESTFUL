from register_restful_api import app
from API.view import register_user_api

app.register_blueprint(register_user_api)

if __name__=='__main__':
    app.run(debug=True)
