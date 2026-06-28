from flask import Flask
from dotenv import load_dotenv
import os
from routes import alumnos_bp
from flask import redirect, url_for
from auth import auth_bp
from models import bd, bcrypt, login_manager

load_dotenv()

def create_app():
    app = Flask(__name__)

    database_url = os.getenv("DATABASE_URL")
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    login_manager.init_app(app)
    bcrypt.init_app(app)
    bd.init_app(app)
    app.register_blueprint(alumnos_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        bd.create_all()
        import login

    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app