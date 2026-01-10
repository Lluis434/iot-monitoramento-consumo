from flask import Blueprint, request, jsonify
from extensions import db
from models import Medicao

consumo_bp = Blueprint('consumo', __name__)


@consumo_bp.route('/api/consumo', methods=['POST'])
def receber_consumo():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "JSON inválido ou ausente"}), 400

    campos = ['tensao', 'corrente', 'potencia', 'energia', 'custo', 'anomalia']
    for campo in campos:
        if campo not in data:
            return jsonify({"erro": f"Campo '{campo}' ausente"}), 422

    try:
        medicao = Medicao(
            tensao=float(data['tensao']),
            corrente=float(data['corrente']),
            potencia=float(data['potencia']),
            energia=float(data['energia']),
            custo=float(data['custo']),
            anomalia=bool(data['anomalia'])
        )
    except ValueError:
        return jsonify({"erro": "Tipos de dados inválidos"}), 422

    db.session.add(medicao)
    db.session.commit()

    return jsonify({"status": "recebido"}), 201
