from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Peter', idade=35)
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



if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    #altera_pessoas()
    #excluir_pessoa()
