from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email e senha são obrigatórios'}), 400
    
    usuario = Usuario.query.filter_by(email=data['email']).first()
    
    if not usuario or not usuario.check_password(data['password']):
        return jsonify({'message': 'Credenciais inválidas'}), 401
    
    token = usuario.generate_token()
    
    return jsonify({
        'access_token': token,
        'usuario': usuario.to_dict()
    }), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    identity = get_jwt_identity()
    usuario = Usuario.query.get(identity['id'])
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    return jsonify(usuario.to_dict()), 200
