# pip install requests
# pip install Flask
# implementação com postman

from flask import Flask, jsonify, request#estranhamente eu não precisei desse jsonify
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id': id, 'nome': 'Fernando', 'profissao': 'Desenvolvedor'})

# @app.route('/soma/<int:valor1>/<int:valor2>/') #Ex. /soma/10/10
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})

@app.route('/soma', methods= ['POST', 'GET'] )
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        #print(dados)
        total = sum(dados['valores'])
        return jsonify({'soma': total})

    elif request.method == 'GET':
        total = 10 + 10
        return jsonify({'soma': total})



if __name__ == '__main__':
    app.run(debug=True)
