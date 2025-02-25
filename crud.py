from models import session, Usuario, Livro

# CRUD

# Create
usuario_matheus = Usuario(nome="Matheus", email="schmitzmatheus321@gmail.com", senha="123123")
session.add(usuario_matheus)
session.commit()

usuario_anderson = Usuario(nome="Anderson", email="andin@gmail.com", senha="123123")
session.add(usuario_anderson)
session.commit()

# Read
usuario_matheus = session.query(Usuario).filter_by(nome="Matheus").first()
print(usuario_matheus)
usuario_anderson = session.query(Usuario).filter_by(nome="Anderson").first()
print(usuario_anderson)

# Create Livros
livro = Livro(titulo="Senhor dos Anéis: O Retorno do Rei", paginas="608", dono=usuario_matheus.id)
session.add(livro)
session.commit()

livro2 = Livro(titulo="Harry Potter e a Pedra Filosofal", paginas="208", dono=usuario_anderson.id)
session.add(livro2)
session.commit()