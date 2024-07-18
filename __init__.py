from src.prompt_messages import Prompt_messages
from dotenv import load_dotenv
from flask import Flask
import os

from database.database import db

config = load_dotenv(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

if __name__ == "__main__":
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    prompt_messages = Prompt_messages()
    stack_selection = prompt_messages.caller()
