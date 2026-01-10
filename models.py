from datetime import datetime
from extensions import db

class Medicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tensao = db.Column(db.Float, nullable=False)
    corrente = db.Column(db.Float, nullable=False)
    potencia = db.Column(db.Float, nullable=False)
    energia = db.Column(db.Float, nullable=False)
    custo = db.Column(db.Float, nullable=False)
    anomalia = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
