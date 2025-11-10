from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # 1. Importe o CORS
from modulos_curso import calculo

app = Flask(__name__)

# 2. Configure o CORS para permitir requisições do seu "Go Live"
#    Isso diz ao Flask para permitir que 'http://127.0.0.1:5500'
#    acesse o endpoint '/calcularemprestimo'.
CORS(app, resources={
     r"/calcularemprestimo": {"origins": "http://127.0.0.1:5500"}})

# Rota para a página inicial (se você quiser manter, mas não é mais necessária
# se o frontend está separado)


@app.route('/')
def index():
    # Esta rota não será mais usada pelo "Go Live",
    # mas podemos deixar para teste.
    return "Servidor Flask da API está no ar. Acesse o frontend pelo Go Live."

# Rota da API


@app.route('/calcularemprestimo', methods=['POST'])
def calcular():
    dados = request.get_json()

    try:
        P = float(dados.get('principal'))
        i_anual = float(dados.get('taxa_anual')) / 100
        n_anos = int(dados.get('anos'))
    except (TypeError, ValueError):
        return jsonify({'status': 'erro', 'mensagem': 'Dados de entrada inválidos ou ausentes.'}), 400

    i_mensal = i_anual / 12
    n_meses = n_anos * 12

    try:
        prestacao = calculo.calcular_prestacao(P, i_mensal, n_meses)

        minha_taxa_local = 0.5

        return jsonify({
            'prestacao': prestacao,
            'status': 'sucesso',
            'explicacao': f'O cálculo foi feito pelo módulo `calculo.py` (função `calcular_prestacao`), que por sua vez importou `math.pow` de forma segura. O valor da minha_taxa_local ({minha_taxa_local}) no nosso código Flask não interferiu no módulo.'
        })
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
