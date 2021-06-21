from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


motor = create_engine('sqlite:///activity.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=motor))

Base = declarative_base()
Base.query = db_session.query_property()


class Programadores(Base):
    __tablename__ = 'programadores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80),
                  index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Programador {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self, instance):
        db_session.delete(self)
        db_session.commit()


class Habilidades(Base):
    __tablename__ = 'habilidades'
    id = Column(Integer, primary_key=True)
    nome_habilidade = Column(String(80))

    def __repr__(self):
        return '<Habilidade {}'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self, instance):
        db_session.delete(self)
        db_session.commit()

class ProgramadorHabilidade(Base):
    __tablename__ = 'programadorhabilidade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    programador_id = Column(Integer, ForeignKey('programadores.id'), nullable=False)
    habilidade_id = Column(Integer, ForeignKey('habilidades.id'), nullable=False)


def init_db():
    Base.metadata.create_all(bind=motor)


if __name__ == '__main__':
    init_db()