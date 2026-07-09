from app import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(200), nullable=False)
    perfil = db.Column(db.String(20), default='seller')
    avatar = db.Column(db.String(10), default='J')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    lojas = db.relationship('Loja', back_populates='usuario', lazy=True)
    vendas = db.relationship('Venda', back_populates='usuario', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def generate_token(self):
        return create_access_token(identity={'id': self.id, 'perfil': self.perfil})
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'perfil': self.perfil,
            'avatar': self.avatar,
            'created_at': self.created_at.isoformat()
        }
