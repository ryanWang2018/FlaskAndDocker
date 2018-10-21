from app.extensions import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        """Display when printing a User object"""

        return "<User: {}>".format(self.username)
