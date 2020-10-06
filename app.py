import os
from flask import Flask,render_template,request
from flask import Blueprint

app = Flask(__name__)

core = Blueprint('core',__name__)

@example_blueprint.route('/')
def index():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
