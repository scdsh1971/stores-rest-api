from app import app
from db import db


db.init_app(app)

@app.before_request # runs this before anything else creates db on start up unless it exists already
def create_tables():
    db.create_all()
