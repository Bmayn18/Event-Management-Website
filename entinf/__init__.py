from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.secret_key = "SuperSecretKey"
    bootstrap = Bootstrap(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///EntInfDB.sqlite'
    db.init_app(app)

    csrf.init_app(app)

    from .models import User
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from . import views, events, auth
    app.register_blueprint(views.mainbp)
    app.register_blueprint(events.bp)
    app.register_blueprint(auth.bp)
    
    return app