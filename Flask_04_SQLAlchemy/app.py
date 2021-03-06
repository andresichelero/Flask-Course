from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth  # autenticação básica com login de usuário e senha

auth = HTTPBasicAuth()  # criar auth
app = Flask(__name__)
api = Api(app)


# USUÁRIOS = {
#   'felipe': '321',
#    'romano': '321'
# } #Dicionário de usuários/senhas hardcoded para autenticação

@auth.verify_password
def Verificacao(login, senha):
    # print('Validando usuario e senha: ')
    # print(USUARIOS.get(login) == senha)
    if not (login, senha):
        return False
    # return USUARIOS.get(login) == senha
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json  # Já recebe os dados no formato JSON, mas se receber dados em formato diferente,
        # irá ocorrer erro
        # Atentar a diferentes bibliotecas do Flask: request e Request!
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaPessoa(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()  # CUIDAR PARA NÃO UTILIZAR EM TABELAS GRANDES! Retorna todos os dados da tabela
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoa, '/pessoa/')
api.add_resource(ListaAtividade, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
