from app import db
from datetime import datetime

class Loja(db.Model):
    __tablename__ = 'lojas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(15))
    pdv_sistema = db.Column(db.String(50), default='PharmaConekt')
    status_onboarding = db.Column(db.String(20), default='pendente')
    sugestoes_aceitas = db.Column(db.Integer, default=0)
    alertas_vencimento = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('Usuario', back_populates='lojas')
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'status_onboarding': self.status_onboarding
        }
