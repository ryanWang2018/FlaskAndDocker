from flask import Flask

from app.extensions import db
from app.helpers import gen_response


# initialize app with config params
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:team24@localhost:5433/team24"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# initialize connection to db
with app.app_context():
    # initialize connection to db
    db.init_app(app)

    # Create all required models for database
    # from app.models.user import User
    # db.create_all()


@app.route("/")
def index():
    return gen_response({'success': True})
