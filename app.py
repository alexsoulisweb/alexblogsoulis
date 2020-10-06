#from blog import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
