import requests
import random
import time

API_URL = "http://localhost:5000/api/consumo"
TARIFA = 0.85  # R$/kWh (valor médio Brasil)

energia_acumulada = 0.0
tempo_anterior = time.time()

contador_ciclos = 0  # 🔹 ALTERAÇÃO: contador para forçar anomalias periódicas

while True:
    contador_ciclos += 1  # 🔹 ALTERAÇÃO: incrementa a cada envio

    # Tempo decorrido em horas
    tempo_atual = time.time()

    # 🔹 ALTERAÇÃO: fator de aceleração do tempo (DEMO)
    # Multiplicamos o delta por 10 para a energia crescer mais rápido
    delta_horas = ((tempo_atual - tempo_anterior) / 3600) * 10
    # Para desfazer: remova o "* 10"
    tempo_anterior = tempo_atual

    # Simulação de medições elétricas
    tensao = random.uniform(210, 230)  # Volts

    # 🔹 ALTERAÇÃO: geração de picos de corrente para simular anomalias
    if contador_ciclos % 6 == 0:
        # A cada 6 ciclos gera um pico proposital
        corrente = random.uniform(15, 20)  # consumo anormal
    else:
        corrente = random.uniform(2, 8)    # consumo normal

    # Potência instantânea (W)
    potencia = tensao * corrente

    # Energia acumulada (kWh)
    energia_acumulada += (potencia / 1000) * delta_horas

    # Custo acumulado (R$)
    custo = energia_acumulada * TARIFA

    # 🔹 ALTERAÇÃO: anomalia fica claramente visível na dashboard
    anomalia = potencia > 2500  # acima de 2,5 kW

    payload = {
        "tensao": round(tensao, 2),
        "corrente": round(corrente, 2),
        "potencia": round(potencia, 2),
        "energia": round(energia_acumulada, 6),
        "custo": round(custo, 2),
        "anomalia": anomalia
    }

    try:
        response = requests.post(API_URL, json=payload)
        print("Enviado:", payload, "| Status:", response.status_code)
    except Exception as e:
        print("Erro ao enviar:", e)

    time.sleep(5)  # envio a cada 5 segundos
