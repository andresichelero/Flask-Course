from flask import Flask     #Importa a biblioteca Flask
app = Flask(__name__)   #Criação de um app Flask, de nome "__name__"


@app.route("/<numero>", methods = ['GET', 'POST'])  #Define a rota dos requests HTTP
def ola(numero):  #Criação da primeira rota do app, na função ola
    return 'Olá mundo. {}' .format(numero)


if __name__ == "__main__":  #Executa o aplicativo, somente se ele for o projeto principal
    app.run(debug=True)
