from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# API ESCRITA DO ZERO COMO EXERCÍCIO DE PRÁTICA DO CURSO PYTHON - FLASK

lista = [
    {
        'id': '0',
        'responsavel': 'Joao',
        'tarefa': 'Resolver calculos de matematica',
        'status': 'incompleto'
    },
    {
        'id': '1',
        'responsavel': 'Maria',
        'tarefa': ['Cadastrar novos usuarios no programa', 'Enviar os relatorios por email'],
        'status': 'concluido'
    }
]


# Realiza a consulta do cadastro das tarefas, adiciona novas tarefas/informações, e também as deleta
@app.route('/tarefa/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def tara(id):
    if request.method == 'GET':
        try:
            response = lista[id]
        except IndexError:
            mensagem = 'ID de tarefa não existente'.format(id)
            response = {'status': 'Erro: Tarefa nao existe', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido: procure um administrador'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        lista[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        lista.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})


# Lista todas e permite criar novas tarefas
@app.route('/tarefa/', methods=['POST', 'GET'])
def tera():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(lista)
        dados['id'] = posicao
        lista.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro incluído'})
    elif request.method == 'GET':
        return jsonify(lista)


if __name__ == '__main__':
    app.run(debug=True)
