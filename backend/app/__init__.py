from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    CORS(app)
    
    from app.routes.auth import auth_bp
    from app.routes.produtos import produtos_bp
    from app.routes.vendas import vendas_bp
    from app.routes.clientes import clientes_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(produtos_bp, url_prefix='/api/produtos')
    app.register_blueprint(vendas_bp, url_prefix='/api/vendas')
    app.register_blueprint(clientes_bp, url_prefix='/api/clientes')
    
    return app
