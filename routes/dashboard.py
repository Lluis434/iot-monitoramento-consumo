from flask import Blueprint, jsonify
from sqlalchemy import func
from extensions import db
from models import Medicao

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/api/dashboard/resumo', methods=['GET'])
def resumo():
    total_energia = db.session.query(func.sum(Medicao.energia)).scalar() or 0
    total_custo = db.session.query(func.sum(Medicao.custo)).scalar() or 0
    ultima = Medicao.query.order_by(Medicao.timestamp.desc()).first()

    return jsonify({
        "ultima_medicao": {
            "tensao": ultima.tensao,
            "corrente": ultima.corrente,
            "potencia": ultima.potencia,
            "energia": ultima.energia,
            "custo": ultima.custo,
            "anomalia": ultima.anomalia,
            "timestamp": ultima.timestamp.isoformat()
        } if ultima else None,
        "energia_total_kwh": round(total_energia, 4),
        "custo_total": round(total_custo, 2)
    })
