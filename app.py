import os
from flask import Flask, request, abort

app = Flask(__name__)

# import declared routes
import views



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
