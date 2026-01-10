from flask import Blueprint, jsonify
from models import Medicao

alertas_bp = Blueprint('alertas', __name__)


# ---------------------------
# GET - Listar todos os alertas
# ---------------------------
@alertas_bp.route('/api/alertas', methods=['GET'])
def listar_alertas():
    alertas = Medicao.query.filter_by(anomalia=True) \
        .order_by(Medicao.timestamp.desc()) \
        .all()

    return jsonify([
        {
            "id": a.id,
            "potencia": a.potencia,
            "tensao": a.tensao,
            "corrente": a.corrente,
            "energia": a.energia,
            "custo": a.custo,
            "timestamp": a.timestamp.isoformat()
        } for a in alertas
    ])
