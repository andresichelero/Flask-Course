from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades

import json

#Não é necessário importar jsonify, pois flask_restful reconhece JSON internamente

app = Flask(__name__)
api = Api(app) #Passo extra no flask_restful

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


class Desenvolvedor(Resource): #Necessária a criação de uma classe
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor não existente'.format(id)
            response = {'status': 'erro de consulta', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido: procure um administrador'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


#lista todos os desenvolvedores e permite registrar um novo desenvolvedor

class ListaDesenvolvedores(Resource):
    def get(self):
        return devs
    def post(self):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return devs[posicao]

#Funcionando como @app.route, a linha 'api.add_resource' define qual classe e qual rota de URI que utilizaremos
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)