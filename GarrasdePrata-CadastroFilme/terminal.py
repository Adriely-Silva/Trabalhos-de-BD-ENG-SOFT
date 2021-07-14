
class Terminal:
    def sobre():
        print("\nCadastro de filmes - Garras de Prata")
        print("...........................................................................")
        print("Sobre as Garras de Prata\nNossa aplicação é um cadastro de filmes no qual você poderá adicionar e avaliar os filmes que gosta muito e adora e também aqueles que você nem gosta tanto. Além de inserir atores, diretores e produtores. ")
        print("...........................................................................\n")
        print("Escolha o que quer fazer:")
        print("A - Inserir os dados\nB - Consultar os dados\nC - Alterar os dados\nD - Deletar os dados\nE - Os filmes em ordem alfabética\nF - Média de notas dos filmes\nG - Filmes e seus diretores\nH - Buscar o filme pelo nome do diretor\n")
        
    def tabela_diretor():
        print("\n1- O cadastro do(a) diretor(a) terá os seguintes campos para preencher, respectivamente:")   
        print("---------------------------------------------------------------------------")
        print("# Código(idDiretor)\n# Nome\n# Data do Nascimento")
        print("---------------------------------------------------------------------------\n\n")
    
    def tabela_filme():
        print("\n2- O cadastro do filme terá os seguintes campos para preencher, respectivamente:")
        print("---------------------------------------------------------------------------")
        print("# Código(idFilme)\n# Título\n# Gênero(s)\n# Ano\n# Classificção Indicativa\n# Duração\n# Código do Diretor")   
        print("---------------------------------------------------------------------------\n\n")

    def tabela_nota():
        print("\n3- O cadastro da nota terá os seguintes campos para preencher, respectivamente:")
        print("---------------------------------------------------------------------------")
        print("# Código(idNota)\n# Nota(Avaliação 10/10)\n# Código do Filme") 
        print("---------------------------------------------------------------------------\n\n")
    
    def tabela_produtora():
        print("\n4- O cadastro da produtora terá os seguintes campos para preencher, respectivamente:")
        print("---------------------------------------------------------------------------")   
        print("# Código(idProdutora\n# Nome")
        print("---------------------------------------------------------------------------\n\n")
    
    def tabela_ator():
        print("\n5- O cadastro do(a) ator/atriz terá os seguintes campos para preencher, respectivamente:")   
        print("---------------------------------------------------------------------------")
        print("# Código(idDiretor)\n# Nome\n# Data do Nascimento")
        print("---------------------------------------------------------------------------")