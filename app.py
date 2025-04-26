from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

def gerar_senha_significativa(nome_mae, nome_pet, numero_casa):
    parte_mae = nome_mae.strip()[0].upper()
    parte_pet = nome_pet.strip()[0].upper()

    senha = f"{parte_mae}{parte_pet}Casa{numero_casa}"

    simbolo = random.choice(['@', '#', '$', '%', '&', '*', '!'])
    senha += simbolo

    return senha

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
      <meta charset="UTF-8">
      <title>Gerador de Senha</title>
      <style>
        body {
          background-color: #1e1e2f;
          color: #fff;
          font-family: Arial, sans-serif;
          text-align: center;
          padding-top: 50px;
        }
        form {
          background: #2c2c3e;
          padding: 20px;
          border-radius: 10px;
          display: inline-block;
        }
        input, button {
          padding: 10px;
          margin: 10px;
          border: none;
          border-radius: 5px;
        }
        input {
          width: 250px;
        }
        button {
          background-color: #ff4081;
          color: white;
          cursor: pointer;
        }
      </style>
    </head>
    <body>
      <h1>Gerador de Senha Segura</h1>
      <form action="/gerar_senha" method="post">
        <input type="text" name="nome_mae" placeholder="Nome da sua mãe" required><br>
        <input type="text" name="nome_pet" placeholder="Nome do seu pet" required><br>
        <input type="text" name="numero_casa" placeholder="Número da casa/apto" required><br>
        <button type="submit">Gerar Senha</button>
      </form>
    </body>
    </html>
    ''')

@app.route('/gerar_senha', methods=['POST'])
def gerar():
    try:
        nome_mae = request.form['nome_mae']
        nome_pet = request.form['nome_pet']
        numero_casa = request.form['numero_casa']
        senha = gerar_senha_significativa(nome_mae, nome_pet, numero_casa)
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
          <meta charset="UTF-8">
          <title>Senha Gerada</title>
          <style>
            body {
              background-color: #1e1e2f;
              color: #fff;
              font-family: Arial, sans-serif;
              text-align: center;
              padding-top: 50px;
            }
            .container {
              background: #2c2c3e;
              padding: 20px;
              border-radius: 10px;
              display: inline-block;
            }
            .senha {
              font-size: 24px;
              font-weight: bold;
              margin: 20px 0;
              color: #ff4081;
            }
            button {
              padding: 10px 20px;
              background-color: #ff4081;
              border: none;
              color: white;
              border-radius: 5px;
              cursor: pointer;
            }
          </style>
        </head>
        <body>
          <div class="container">
            <h1>Sua Senha Gerada:</h1>
            <div class="senha">{{ senha }}</div>
            <a href="/"><button>Voltar</button></a>
          </div>
        </body>
        </html>
        ''', senha=senha)
    except Exception as e:
        return f"<h1>Erro: {e}</h1>"

if __name__ == '__main__':
    app.run(debug=True)