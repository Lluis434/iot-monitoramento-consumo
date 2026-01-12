Monitoramento Inteligente de Consumo Elétrico utilizando IoT

Este projeto apresenta o desenvolvimento de um sistema IoT para monitoramento inteligente de consumo elétrico, baseado em uma arquitetura em três camadas (Dispositivo, Borda e Nuvem).
Devido às limitações do ambiente de simulação (Tinkercad), a lógica de coleta de dados e pré-processamento é simulada em um script Python, que representa o comportamento do Arduino em um cenário real.

1. Visão Geral do Sistema

O sistema simula um ambiente de monitoramento elétrico residencial, no qual medições de tensão e corrente seriam coletadas por sensores conectados a um microcontrolador Arduino.
Como o Tinkercad não permite requisições HTTP, um script Python é utilizado para simular:

A coleta das medições elétricas

O pré-processamento local dos dados

O envio das informações para a aplicação web via API REST

2. Arquitetura do Sistema

A arquitetura segue o modelo de IoT em três camadas:

2.1 Camada de Dispositivos (Percepção)

Sensores simulados de tensão e corrente

Microcontrolador Arduino UNO (simulado no Tinkercad)

Responsável conceitualmente pela coleta dos dados elétricos

2.2 Camada de Borda (Edge Computing)

Simulada em um script Python

Representa o comportamento do Arduino em um ambiente real

Realiza:

Cálculo de potência instantânea (W)

Cálculo de energia consumida (kWh)

Estimativa de custo (R$)

Detecção de anomalias de consumo

Envia os dados processados para a camada de nuvem via HTTP

⚠️ Em um cenário real, essa camada seria executada diretamente no Arduino ou em um gateway físico.

2.3 Camada de Nuvem (Plataforma IoT)

Aplicação web desenvolvida em Flask

Persistência dos dados em banco de dados SQLite

Disponibilização de dashboards e histórico de alertas

3. Funcionalidades do Sistema

Simulação da coleta de medições elétricas

Pré-processamento local dos dados simulados

Armazenamento histórico de consumo

Detecção automática de anomalias

Dashboards web com:

Consumo instantâneo

Energia acumulada

Custo estimado

Histórico de alertas

Consumo por período (dia, semana e mês)

4. Tecnologias Utilizadas

Python

Flask

SQLAlchemy

SQLite

HTML5 e CSS3

Arduino (simulação no Tinkercad)

PROJETO_IOT/
│
├── app.py                     # Inicialização da aplicação Flask e registro das rotas
├── extensions.py              # Configuração e inicialização do SQLAlchemy
├── models.py                  # Modelos do banco de dados (Medições de consumo)
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação do projeto
├── .gitignore                 # Arquivos ignorados pelo Git
│
├── gateway/
│   └── gateway_simulado.py    # Simula o Arduino + camada de borda
│                              # (coleta, pré-processamento e envio via HTTP)
│
├── instance/
│   └── database.db            # Banco de dados SQLite
│
├── routes/                    # Rotas (Blueprints) da aplicação
│   ├── consumo.py             # API de recebimento das medições
│   ├── dashboard.py           # Rotas dos dashboards
│   └── alertas.py             # Rotas e API do histórico de alertas
│
├── templates/                 # Templates HTML
│   ├── index.html             # Página inicial (Home)
│   ├── dashboard.html         # Dashboard principal
│   ├── dashboard_alertas.html # Dashboard de histórico de alertas
│   └── consumo_periodos.html  # Dashboard de consumo por período
│
├── static/                    # Arquivos estáticos (CSS e JS)
│   ├── index.css              # Estilo da página inicial
│   ├── style.css              # Estilo geral dos dashboards
│   ├── alertas.css            # Estilo do dashboard de alertas
│   ├── periodos.css           # Estilo do consumo por período
│   ├── home_button.css        # Botão de navegação para Home
│   └── periodos.js            # Lógica JS do consumo por período
│
└── venv/                      # Ambiente virtual Python

6. Execução do Sistema
6.1 Instalação das Dependências
pip install -r requirements.txt

6.2 Execução da Aplicação Web
python app.py

6.3 Execução do Simulador (Dispositivo + Borda)
python gateway/gateway_simulado.py

6.4 Acesso à Interface Web
http://localhost:5000

7. Observação Importante

Este projeto possui caráter acadêmico e didático, com foco na demonstração dos conceitos de:

Internet das Coisas (IoT)

Computação em Borda

Arquitetura em três camadas

Monitoramento energético

O arquivo gateway/gateway_simulado.py representa conceitualmente as camadas de Dispositivo e Borda, sendo responsável por:

Simular sensores de tensão e corrente

Executar o pré-processamento local (potência, energia, custo e anomalias)

Enviar os dados para a API Flask via HTTP

Essa abordagem foi adotada devido à limitação do Tinkercad, que não permite requisições HTTP diretas.

A substituição do script simulador por um Arduino real exigiria apenas a adaptação do envio HTTP dos dados para a API Flask.