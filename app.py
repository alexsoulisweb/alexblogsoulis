import os
import json
from flask import current_app as app

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template("core.base")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
