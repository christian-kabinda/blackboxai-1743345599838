from flask import Blueprint
from app.api import jobs

bp = Blueprint('api', __name__)

def init_app(app):
    app.register_blueprint(jobs.bp)
    # Additional blueprints will be registered here