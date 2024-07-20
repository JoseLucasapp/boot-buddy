from src.main import Booty_buddy
from dotenv import load_dotenv
from flask import Flask
import os

from database.database import db
from src.system_settings import System_settings

System_settings.clear_terminal()

config = load_dotenv(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app=app)

if __name__ == "__main__":

    with app.app_context():
        db.create_all()
        prompt_messages = Booty_buddy()

        try:
            prompt_messages.stack()
        except Exception as e:
            print(f"Erro: {e}")
