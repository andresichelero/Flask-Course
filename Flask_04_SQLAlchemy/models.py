# Arquivo .py onde estarão as classes que referenciam o banco de dados

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
# Responsáveis por criar as sessões do banco de dados para realizar as consultas, etc. - Cada consulta/operação é uma
# nova sessão/instância.
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40),
                  index=True)  # Opção index facilita e aumenta a rapidez das consultas por esse parametro, no caso,
    # nome.
    idade = Column(Integer)

    def __repr__(
            self):  # É uma função opcional e estabelece o padrão de retorno dos dados da tabela ao realizar uma busca na tabela correspondente.
        return '<Pessoa {}>'.format(self.nome)

    # Permite que eu de commit na inserção sem ter que manualmente escrever na função 'insere_pessoas' no arquivo 'utils'
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))  # FK, Chave Estrangeira
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    # Permite que eu de commit na inserção sem ter que manualmente escrever na função 'insere_pessoas' no arquivo 'utils'
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)  # Unique não permite dois usuários com o mesmo nome
    senha = Column(String(20))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
