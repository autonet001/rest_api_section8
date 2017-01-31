from app import app
from db import db

db.init_app(app)

@app.before_first_request #runs method before first request to app
def create_tables():
    db.create_all()
