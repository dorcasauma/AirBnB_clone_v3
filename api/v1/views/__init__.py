from flask import Blueprint

# Create the Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import of everything in api.v1.views.index
from api.v1.views.index import *
