from flask import Flask

from main.routes import main
from auth.routes import auth


app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')