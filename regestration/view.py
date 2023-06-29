from regestration import app
from regestration.api.view import reg

app.register_blueprint(reg)

if __name__=='__main__':
    app.run(debug=True)

