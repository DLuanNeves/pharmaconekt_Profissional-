from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/', methods=['GET'])
@jwt_required()
def listar_produtos():
    # Retorna lista de produtos mockada para teste
    return jsonify([
        {'id': 1, 'nome': 'Paracetamol 500mg', 'preco': 8.50, 'estoque': 52},
        {'id': 2, 'nome': 'Dipirona 1g', 'preco': 12.90, 'estoque': 38},
        {'id': 3, 'nome': 'Ibuprofeno 600mg', 'preco': 15.50, 'estoque': 25}
    ]), 200

@produtos_bp.route('/', methods=['POST'])
@jwt_required()
def criar_produto():
    data = request.get_json()
    return jsonify({'message': 'Produto criado com sucesso!', 'data': data}), 201
