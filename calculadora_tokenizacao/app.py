from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_custos(input_tokens, cached_tokens, output_tokens, preco_input, preco_cached, preco_output, reqs_por_usuario, usuarios, dias):
    custo_input = (input_tokens / 1_000_000) * preco_input
    custo_cached = (cached_tokens / 1_000_000) * preco_cached
    custo_output = (output_tokens / 1_000_000) * preco_output
    custo_requisicao = custo_input + custo_cached + custo_output
    custo_diario_usuario = custo_requisicao * reqs_por_usuario
    custo_diario_total = custo_diario_usuario * usuarios
    custo_periodo = custo_diario_total * dias
    return {
        'custo_input': custo_input,
        'custo_cached': custo_cached,
        'custo_output': custo_output,
        'custo_requisicao': custo_requisicao,
        'custo_diario_usuario': custo_diario_usuario,
        'custo_diario_total': custo_diario_total,
        'custo_periodo': custo_periodo
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    valores = {
        'input_tokens': 1500,
        'cached_tokens': 500,
        'output_tokens': 700,
        'preco_input': 1.00,
        'preco_cached': 0.10,
        'preco_output': 5.00,
        'reqs_por_usuario': 8,
        'usuarios': 2500,
        'dias': 30
    }
    if request.method == 'POST':
        for k in valores:
            valores[k] = float(request.form[k])
        resultado = calcular_custos(
            valores['input_tokens'], valores['cached_tokens'], valores['output_tokens'],
            valores['preco_input'], valores['preco_cached'], valores['preco_output'],
            valores['reqs_por_usuario'], valores['usuarios'], valores['dias']
        )
    return render_template('index.html', valores=valores, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
