from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Jesus', idade='2021')
    print(pessoa)
    pessoa.save()  # método da própria classe Pessoas, onde há a def save


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

    # print(pessoa) para exibir todos os itens da tabela
    # pessoa = Pessoas.query.filter_by(nome='Jesus')
    # Filter_by criará uma lista de objetos correspondentes, e para
    # acessar, precisa de um FOR, ou, escrever da seguinte maneira:
    # pessoa = Pessoas.query.filter_by(nome='Jesus').first()  #assim ele mostrará apenas o primeiro elemento.
    # print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Romano').first()
    # print(pessoa.idade)


def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Romano').first()
    # pessoa.idade = 34
    # pessoa.nome = 'Romano'
    pessoa.save()


def delete_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Jesus').first()
    pessoa.delete()


def insereUsuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consultaUsuarios():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == '__main__':
    insereUsuario('Rafael', '1234')
    insereUsuario('Felipe', '4321')
    consultaUsuarios()
    #insere_pessoas()
    #consulta_pessoas()
    # altera_pessoas()
    #delete_pessoas()
    #consulta_pessoas()
