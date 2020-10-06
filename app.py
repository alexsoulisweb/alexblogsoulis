from flask import Flask
from flask import Blueprint
from flask import current_app as app


core = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

if __name__ == '__main__':
    app.run(debug=True)
