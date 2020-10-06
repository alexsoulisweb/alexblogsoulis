
from flask import Blueprint

blog = Blueprint(
    'site',
    __name__,
    template_folder='templates',
    static_folder='static'
)

import .views
