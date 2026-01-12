async function carregarConsumo() {
    try {
        const response = await fetch('/api/dashboard/consumo-periodos');
        const data = await response.json();

        document.getElementById('dia-energia').innerText = data.dia.energia.toFixed(4);
        document.getElementById('dia-custo').innerText = data.dia.custo.toFixed(2);

        document.getElementById('semana-energia').innerText = data.semana.energia.toFixed(4);
        document.getElementById('semana-custo').innerText = data.semana.custo.toFixed(2);

        document.getElementById('mes-energia').innerText = data.mes.energia.toFixed(4);
        document.getElementById('mes-custo').innerText = data.mes.custo.toFixed(2);

    } catch (e) {
        console.error('Erro ao carregar consumo:', e);
    }
}

carregarConsumo();
setInterval(carregarConsumo, 10000);
