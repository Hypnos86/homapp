from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicjalizacja aplikacji Flask
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# Konfiguracja bazy danych SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicjalizacja SQLAlchemy
db = SQLAlchemy(app)

# Importujemy plik z trasami
from app import routes  # Import tras
