from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {
        'id':'0',
        'nome':'Rafael',
     'habilidades':['Python', 'Flask']
     },
    {
        'id':'1',
        'nome':'Andre',
     'habilidades':['Python', 'Nenhuma']}
]

#devolve como resposta um desenvolvedor, via ID, além de adicionar ou deletar

@app.route('/dev/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor não existente'.format(id)
            response = {'status':'erro de consulta', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido: procure um administrador'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido'})

#lista todos os desenvolvedores e permite registrar um novo desenvolvedor

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify(devs[posicao], {'status':'sucesso', 'mensagem': 'registro inserido'})
    elif request.method == 'GET':
        return jsonify(devs)

if __name__ == '__main__':
    app.run(debug=True)