from flask import Blueprint, jsonify
from flask import Blueprint, jsonify, render_template
from sqlalchemy import func
from extensions import db
from models import Medicao
from datetime import datetime, timedelta


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

@dashboard_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@dashboard_bp.route('/dashboard/alertas')
def dashboard_alertas():
    return render_template('dashboard_alertas.html')



@dashboard_bp.route('/api/dashboard/consumo-periodos', methods=['GET'])
def consumo_por_periodo():
    agora = datetime.now()

    inicio_dia = agora.replace(hour=0, minute=0, second=0, microsecond=0)
    inicio_semana = inicio_dia - timedelta(days=inicio_dia.weekday())
    inicio_mes = inicio_dia.replace(day=1)

    def soma_energia(inicio):
        return db.session.query(
            func.sum(Medicao.energia)
        ).filter(
            Medicao.timestamp >= inicio
        ).scalar() or 0

    def soma_custo(inicio):
        return db.session.query(
            func.sum(Medicao.custo)
        ).filter(
            Medicao.timestamp >= inicio
        ).scalar() or 0

    return jsonify({
        "dia": {
            "energia": round(soma_energia(inicio_dia), 4),
            "custo": round(soma_custo(inicio_dia), 2)
        },
        "semana": {
            "energia": round(soma_energia(inicio_semana), 4),
            "custo": round(soma_custo(inicio_semana), 2)
        },
        "mes": {
            "energia": round(soma_energia(inicio_mes), 4),
            "custo": round(soma_custo(inicio_mes), 2)
        }
    })

@dashboard_bp.route('/consumo-periodos')
def pagina_consumo_periodos():
    return render_template('consumo_periodos.html')
