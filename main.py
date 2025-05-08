from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/media', methods=['POST'])
def media():
    try:
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        media = round((nota1 + nota2 + nota3) / 3, 2)

        if media >= 7 and media < 11:
            situacao = 'aprovado'
        elif media >= 0 and media < 7:
            situacao = 'reprovado'
        else:
            situacao = 'média inválida'

        return render_template('index.html', media=media, situacao=situacao)
    except ValueError as e:
        return render_template('erro.html', mensagem=f"Entrada inválida: {e}")
    finally:
        print("obrigado por usar o programa ")


if __name__ == '__main__':
    app.run(debug=True)