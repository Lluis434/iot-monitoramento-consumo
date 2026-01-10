# Monitoramento Inteligente de Consumo Elétrico

Sistema IoT para monitoramento de consumo elétrico utilizando Arduino, Flask e dashboards web.

## Arquitetura
- Dispositivo: Arduino (simulado no Tinkercad)
- Borda: Processamento local (potência, energia, anomalias)
- Nuvem: API Flask, banco de dados e dashboards

## Funcionalidades
- Recebimento de medições (tensão, corrente, potência)
- Armazenamento em banco de dados
- Detecção de consumo anormal
- Dashboard de consumo
- Listagem de alertas

## Tecnologias
- Python
- Flask
- SQLAlchemy
- SQLite

## Execução
```bash
pip install -r requirements.txt
python app.py
