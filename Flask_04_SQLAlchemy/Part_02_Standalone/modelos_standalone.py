from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


motor = create_engine('sqlite:///activity.db')
db_sessao = scoped_session(sessionmaker(autocommit=True,
                                        bind=motor))

Base = declarative_base()
Base.query = db_sessao.query_property()


class Programadores(Base):
    __tablename__ = 'programadores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40),
                  index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Programador {}'.format(self.nome)

    def save(self):
        db_sessao.add(self)
        db_sessao.commit()

    def delete(self, instance):
        db_sessao.delete(self)
        db_sessao.commit()


class Habilidades(Base):
    __tablename__ = 'habilidades'
    id_habilidades = Column(Integer, primary_key=True)
    nome_habilidade = Column(String(80))

    def __repr__(self):
        return '<Habilidade {}'.format(self.nome)

    def save(self):
        db_sessao.add(self)
        db_sessao.commit()

    def delete(self, instance):
        db_sessao.delete(self)
        db_sessao.commit()


def init_db():
    Base.metadata.create_all(bind=motor)


if __name__ == '__main__':
    init_db()