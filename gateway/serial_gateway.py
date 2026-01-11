import requests
import random
import time

API_URL = "http://localhost:5000/api/consumo"

while True:
    # gera valores aleatórios para simular o Arduino
    tensao = random.uniform(210, 230)
    corrente = random.uniform(0, 10)
    potencia = tensao * corrente
    energia = random.uniform(0, 5)
    custo = energia * 0.75  # preço fictício
    anomalia = random.choice([True, False])

    payload = {
        "tensao": tensao,
        "corrente": corrente,
        "potencia": potencia,
        "energia": energia,
        "custo": custo,
        "anomalia": anomalia
    }

    try:
        response = requests.post(API_URL, json=payload)
        print("Enviado:", payload, "| Status:", response.status_code)
    except Exception as e:
        print("Erro ao enviar:", e)

    time.sleep(5)  # envia a cada 5 segundos
