from flask import Blueprint
from flask_restful import Api

API_VERSION_V1 = 1

api_bp = Blueprint('api', __name__)
api_v1 = Api(api_bp)
