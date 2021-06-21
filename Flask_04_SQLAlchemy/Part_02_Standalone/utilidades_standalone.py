from modelos_standalone import Programadores


def insere_programadores():
    dev = Programadores(nome='Tadeu', idade='20')
    print(dev)
    dev.save()


def consulta_programadores():
    dev = Programadores.query.all()
    print(dev)

    # print(pessoa) para exibir todos os itens da tabela
    # pessoa = Pessoas.query.filter_by(nome='Jesus')
    # Filter_by criará uma lista de objetos correspondentes, e para
    # acessar, precisa de um FOR, ou, escrever da seguinte maneira:
    # pessoa = Pessoas.query.filter_by(nome='Jesus').first()  #assim ele mostrará apenas o primeiro elemento.
    # print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Romano').first()
    # print(pessoa.idade)


def altera_programadores():
    dev = Programadores.query.filter_by(nome='Ricardo').first()
    dev.idade = 34
    dev.nome = 'Romano'
    dev.save()


def delete_programadores():
    dev = Programadores.query.filter_by(nome='Jesus').first()
    dev.delete()


if __name__ == '__main__':
    #insere_programadores()
    consulta_programadores()
    altera_programadores()
    consulta_programadores()