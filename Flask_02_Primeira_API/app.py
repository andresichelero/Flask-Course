from flask import Flask, jsonify, request
import json
app = Flask(__name__)


@app.route('/<int:id>')   #Com a tipagem 'int', é impossível verificar com outros dados além da ID
def pessoas(id):
    return jsonify({'id':id, 'nome':'Rafael', 'profissao':'Desenvolvedor'}) #This function turns the JSON output into a Response object,
# with the application/json mimetype. For convenience, it also converts multiple arguments into an array or multiple keyword arguments into a dict.
#This means that both jsonify(1,2,3) and jsonify([1,2,3]) serialize to [1,2,3].

#@app.route('/soma/<int:valor1>/<int:valor2>')
#def soma(valor1, valor2):
#    return jsonify({'soma':valor1+valor2})

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma':total})


if __name__ == '__main__':
    app.run(debug=True)