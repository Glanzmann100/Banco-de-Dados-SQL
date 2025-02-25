from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

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

Base.metadata.create_all(bind=db)

# CRUD

# Create
usuario_matheus = Usuario(nome="Matheus", email="schmitzmatheus321@gmail.com", senha="123123")
session.add(usuario_matheus)
session.commit()

usuario_anderson = Usuario(nome="Anderson", email="andin@gmail.com", senha="123123")
session.add(usuario_anderson)
session.commit()

# Read
usuario_matheus = session.query(Usuario).filter_by(email="schmitzmatheus321@gmail.com").first()
print(usuario_matheus)
usuario_anderson = session.query(Usuario).filter_by(email="andin@gmail.com").first()
print(usuario_anderson)

# Create Livros
livro = Livro(titulo="Senhor dos Anéis: O Retorno do Rei", paginas="608", dono=usuario_matheus.id)
session.add(livro)
session.commit()

livro2 = Livro(titulo="Harry Potter e a Pedra Filosofal", paginas="208", dono=usuario_anderson.id)
session.add(livro2)
session.commit()