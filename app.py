from flask import Flask, render_template
from extensions import db
from routes.consumo import consumo_bp
from routes.dashboard import dashboard_bp
from routes.alertas import alertas_bp


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(consumo_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(alertas_bp)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
