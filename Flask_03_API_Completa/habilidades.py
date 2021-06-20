#Cria uma lista de habilidades disponíveis para consulta, utilizados
#no arquivo app_restful.py

from flask_restful import Resource

lista_habilidades = ['Python', 'Flask', 'Java', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades