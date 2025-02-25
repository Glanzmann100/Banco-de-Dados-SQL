from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco de dados
db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# Tabelas
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo  

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', ativo={self.ativo})>"

class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True) 
    titulo = Column("titulo", String)  
    paginas = Column("paginas", String)
    dono = Column("dono", ForeignKey("usuarios.id"))
    
    def __init__(self, titulo, paginas, dono):
        self.titulo = titulo
        self.paginas = paginas
        self.dono = dono

    def __repr__(self):
        return f"<Livro(id={self.id}, titulo='{self.titulo}', paginas='{self.paginas}', dono={self.dono})>"

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=db)