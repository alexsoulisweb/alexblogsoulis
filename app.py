import os
from blog import app
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
