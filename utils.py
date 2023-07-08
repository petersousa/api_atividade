from models import Pessoas, Usuarios

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Tiao', idade=59)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoas():
    #pessoa = Pessoas.query.all()
    '''for i in  pessoa: #Listando o nome das pessoas
        print(i.nome)'''

    '''
    pessoa = Pessoas.query.filter_by(nome='Daniel')
    for p in pessoa:
        print(p)'''
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Peter').first() # mostra a idade da pessoa especificada
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Daniel').first()
    pessoa.idade = 4
    pessoa.save()

# Exclui dados na tabela pessoa
def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Daniel').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()
    print(usuario)

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('peter', 123)
    insere_usuario('daniel', 4321)
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoas()
    #excluir_pessoa()
