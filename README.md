# Monitoramento Inteligente de Consumo Elétrico

Sistema IoT para monitoramento de consumo elétrico baseado no conceito de **arquitetura em três camadas**, utilizando **Arduino (simulado)**, **processamento em borda** e **aplicação web em Flask** para visualização e análise dos dados.

---

## Visão Geral

O projeto tem como objetivo simular um sistema de monitoramento inteligente de consumo elétrico capaz de:
- Coletar medições de tensão e corrente
- Calcular potência e consumo energético
- Detectar padrões anômalos de consumo
- Armazenar dados históricos
- Exibir dashboards interativos via aplicação web

Devido às limitações do **Tinkercad**, que não permite requisições HTTP, a **lógica de coleta de dados e pré-processamento também é simulada em script Python**, representando o comportamento do dispositivo e da camada de borda.

---

## Arquitetura do Sistema

O sistema segue o modelo de **Arquitetura IoT em Três Camadas**:

### 🔹 Camada de Percepção (Dispositivo)
- Representada por um Arduino simulado
- Sensores de tensão e corrente
- Coleta contínua de dados elétricos

### 🔹 Camada de Borda
- Simulada no script `gateway_simulado.py`
- Realiza cálculos de:
  - Potência instantânea
  - Energia consumida
- Identifica comportamentos anômalos
- Envia os dados processados para a aplicação

### 🔹 Camada de Nuvem
- Aplicação web desenvolvida em Flask
- Responsável por:
  - Armazenamento dos dados
  - Exibição de dashboards
  - Histórico de alertas
  - Análises por período (dia, semana e mês)

---

## Funcionalidades

- Simulação da coleta de tensão e corrente
- Cálculo de potência e consumo energético
- Detecção de consumo anormal
- Registro de alertas no banco de dados
- Dashboard de consumo em tempo real
- Visualização de consumo por período
- Histórico de alertas de anomalias

---

## Tecnologias Utilizadas

- **Python**
- **Flask**
- **SQLAlchemy**
- **SQLite**
- **HTML, CSS e JavaScript**

> O detalhamento das tecnologias e suas escolhas é abordado em seções específicas do trabalho.

---

## Estrutura do Projeto

```text
PROJETO_IOT/
├── app.py
├── extensions.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── gateway/
│   └── gateway_simulado.py
│
├── instance/
│   └── database.db
│
├── routes/
│   ├── consumo.py
│   ├── dashboard.py
│   └── alertas.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── dashboard_alertas.html
│   └── consumo_periodos.html
│
├── static/
│   ├── index.css
│   ├── style.css
│   ├── alertas.css
│   ├── periodos.css
│   ├── home_button.css
│   └── periodos.js
│
└── venv/

🚀Execução do Projeto
🧪Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

📦Instalar as dependências
pip install -r requirements.txt

▶️Executar a aplicação Flask
python app.py

🔌Executar o simulador de coleta de dados
💡Em outro terminal:
python gateway/gateway_simulado.py

⚠️Observações Importantes
A comunicação entre dispositivo, borda e nuvem é realizada de forma simulada localmente.
O script gateway_simulado.py representa:

- A coleta de dados dos sensores
- O pré-processamento local
- O envio das informações para a aplicação Flask
- O banco de dados SQLite é criado automaticamente na pasta instance.

🎓 Finalidade do Projeto
Este projeto possui caráter acadêmico e educacional, sendo utilizado para fins de estudo e demonstração de conceitos de IoT em arquitetura de três camadas.