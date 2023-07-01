from Register_API import app
from API.views import register_user_api

app.register_blueprint(register_user_api)

if __name__=='__main__':
    app.run(debug=True)