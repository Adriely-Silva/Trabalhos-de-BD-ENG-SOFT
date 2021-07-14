import pymysql

from diretor_dao import DiretorDao
from diretor import Diretor
from filme_dao import FilmeDao
from filme import Filme
from ator_dao import AtorDao
from ator import Ator
from produtora_dao import ProdutoraDao
from produtora import Produtora
from nota_dao import NotaDao
from nota import Nota

from terminal import Terminal

conexao = pymysql.connect(db = 'cf', user = 'root', passwd = '1234')

#Terminal
tela = Terminal
tela.sobre()

escolha = input("")
if escolha.upper() == 'A':
    
    tela.tabela_diretor()
    tela.tabela_filme()
    tela.tabela_nota()
    tela.tabela_produtora()
    tela.tabela_ator()

    tabela = input("Escolha uma tabela para preencher:\n")
    if tabela == '':
        print("Nenhuma tabela escolhida")

    if tabela == '1':
        print("Digite o código do(a) diretor(a):")
        c = input("")
        print("Digite o nome do(a) diretor(a):")
        n = input("")
        print("Digite a data de nascimento do(a) diretor(a):")
        d = input("")
        diretorDao = DiretorDao(conexao)
        diretorDao.inserir(Diretor(int(c), n, d))
    elif tabela == '2':
        print("Digite o código do filme:")
        c = input("")
        print("Digite o título do filme:")
        t = input("")
        print("Digite o(s) gênero(s) do filme:")
        g = input("")
        print("Digite o ano do filme:")
        a = input("")
        print("Digite a classificação indicativa do filme:")
        ci = input("")
        print("Digite a duração do filme:")
        d = input("")
        print("Digite o código do diretor do filme:")
        cd = input("")
        filmeDao = FilmeDao(conexao)
        filmeDao.inserir(Filme(int(c), t, g, a, ci, d, int(cd)))
    elif tabela == '3':
        print("Digite o código da nota:")
        c = input("")
        print("Digite o valor da nota:")
        n = input("")
        print("Digite o código do filme:")
        cf = input("")
        notaDao = NotaDao(conexao)
        notaDao.inserir(Nota(int(c), n, int(cf)))
    elif tabela == '4':
        print("Digite o código da produtora:")
        c = input("")
        print("Digite o nome da produtora:")
        n = input("")
        produtoraDao = ProdutoraDao(conexao)
        produtoraDao.inserir(Produtora(int(c), n))
    elif tabela == '5':
        print("Digite o código do(a) ator(a):")
        c = input("")
        print("Digite o nome do(a) ator(a):")
        n = input("")
        print("Digite a data de nascimento do(a) ator(a):")
        d = input("")
        atorDao = AtorDao(conexao)
        atorDao.inserir(Ator(int(c), n, d))
    else:
        print("Essa tabela não existe")

if escolha.upper() == 'B':
    print("Tabelas para consultar:")
    print("1 - Diretor\n2 - Filme\n3 - Nota\n4 - Produtora\n5 - Ator/Atriz")
    tabela = input("Selecione o número da tabela que quer consultar:\n")
    if tabela == '' :
        print("Nenhuma tabela selecionada")
    if tabela == '1':
        diretorDao = DiretorDao(conexao)
        diretores = diretorDao.consultar()
        for diretor in diretores:
            print(diretor.to_string())
    elif tabela == '2':
        filmeDao = FilmeDao(conexao)
        filmes = filmeDao.consultar()
        for filme in filmes:
            print(filme.to_string())
    elif tabela == '3':
        notaDao = NotaDao(conexao)
        notas = notaDao.consultar()
        for nota in notas:
            print(nota.to_string())
    elif tabela == '4':
        produtoraDao = ProdutoraDao(conexao)
        produtoras = produtoraDao.consultar()
        for produtora in produtoras:
            print(produtora.to_string())
    elif tabela == '5':
        atorDao = AtorDao(conexao)
        atores = atorDao.consultar()
        for ator in atores:
            print(ator.to_string())
    else:
        print("Essa tabela não existe")

if escolha.upper() == 'C':
    print("Tabelas para consultar:")
    print("1 - Diretor\n2 - Filme\n3 - Nota\n4 - Produtora\n5 - Ator/Atriz")
    tabela = input("Selecione o número da tabela que quer consultar:\n")
    if tabela == '' :
        print("Nenhuma tabela selecionada")
    if tabela == '1':
        id = input("Digite o código do(a) diretor(a) que você quer atualizar:\n")
        diretorDao = DiretorDao(conexao)
        diretores = diretorDao.consultar()
 
        diretor_achado = None
        for diretor in diretores:
            if int(diretor.id) == int(id):
                diretor_achado = diretor
        
        if diretor_achado == None:
            print("Diretor não encontrado")
        else:
            n = input("Atualizar o nome:\n")
            d = input("Atualizar a data de nascimento:\n")
            diretorDao.atualizar(Diretor(diretor_achado.id, n, d))      
    elif tabela == '2':
        id = input("Digite o código do filme que você quer atualizar:\n")
        filmeDao = FilmeDao(conexao)
        filmes = filmeDao.consultar()
        
        filme_achado = None
        for filme in filmes:
            if int(filme.id) == int(id):
                filme_achado = filme
        
        if filme_achado == None:
            print("Filme não encontrado")
        else:
            t = input("Atualizar o título:\n")
            g = input("Atualizar o(s) gênero(s):\n")
            a = input("Atualizar o ano:\n")
            ci = input("Atualizar a classificação indicativa:\n")
            d = input("Atualizar a duração:\n")
            cd = input("Atualizar o código do(a) diretor(a):\n")
            filmeDao.atualizar(Filme(filme_achado.id, t, g, a, ci, d, cd))           
    elif tabela == '3':
        id = input("Digite o código da nota que você quer atualizar:\n")
        notaDao = NotaDao(conexao)
        notas = notaDao.consultar()

        nota_achada = None
        for nota in notas:
            if int(nota.id) == int(id):
                nota_achada = nota
        
        if nota_achada == None:
            print("Nota não encontrada")
        else:
            n = input("Atualizar a nota:\n")
            cf = input("Atualizar o código do filme:\n")
            notaDao.atualizar(Nota(nota_achada.id, n, cf))
    elif tabela == '4':
        id = input("Digite o código da produtora que você quer atualizar:\n")
        produtoraDao = ProdutoraDao(conexao)
        produtoras = produtoraDao.consultar()

        produtora_achada = None
        for produtora in produtoras:
            if int(produtora.id) == int(id):
                produtora_achada = produtora
        
        if produtora_achada == None:
            print("Produtora não encontrada")
        else:
            n = input("Atualizar o nome:\n")
            produtoraDao.atualizar(Produtora(produtora_achada.id, n))          
    elif tabela == '5':
        id = input("Digite o código do(a) ator(a) que você quer atualizar:\n")
        atorDao = AtorDao(conexao)
        atores = atorDao.consultar()

        ator_achado = None
        for ator in atores:
           if int(ator.id) == int(id):
                ator_achado = ator
        
        if ator_achado == None:
            print("Ator(a) não encontrado(a)")
        else:
            n = input("Atualizar o nome:\n")
            d = input("Atualizar a data de nascimento:\n")
            atorDao.atualizar(Ator(ator_achado.id, n, d))
    else:
        print("Essa tabela não existe")

if escolha.upper() == 'D':
    print("Tabelas para consultar:")
    print("1 - Diretor\n2 - Filme\n3 - Nota\n4 - Produtora\n5 - Ator/Atriz")
    tabela = input("Selecione o número da tabela que quer consultar:\n")
    if tabela == '' :
        print("Nenhuma tabela selecionada")
    if tabela == '1':
        id = input("Digite o código do(a) diretor(a) que você quer excluir:\n")
        diretorDao = DiretorDao(conexao)
        diretores = diretorDao.consultar()
 
        diretor_achado = None
        for diretor in diretores:
            if int(diretor.id) == int(id):
                diretor_achado = diretor
        
        if diretor_achado == None:
            print("Diretor não encontrado")
        else:
            diretorDao.excluir(diretor_achado)
    elif tabela == '2':
        id = input("Digite o código do filme que você quer excluir:\n")
        filmeDao = FilmeDao(conexao)
        filmes = filmeDao.consultar()

        filme_achado = None
        for filme in filmes:
            if int(filme.id) == int(id):
                filme_achado = filme
        
        if filme_achado == None:
            print("Diretor não encontrado")
        else:
            filmeDao.excluir(filme_achado)
    elif tabela == '3':
        id = input("Digite o código da nota que você quer excluir:\n")
        notaDao = NotaDao(conexao)
        notas = notaDao.consultar()

        nota_achada = None
        for nota in notas:
            if int(nota.id) == int(id):
                nota_achada = nota
        
        if nota_achada == None:
            print("Nota não encontrada")
        else:
            notaDao.excluir(nota_achada)
    elif tabela == '4':
        id = input("Digite o código da produtora que você quer excluir:\n")
        produtoraDao = ProdutoraDao(conexao)
        produtoras = produtoraDao.consultar()

        produtora_achada = None
        for produtora in produtoras:
            if int(produtora.id) == int(id):
                produtora_achada = produtora
        
        if produtora_achada == None:
            print("Produtora não encontrada")
        else:
            produtoraDao.excluir(produtora_achada)
    elif tabela == '5':
        id = input("Digite o código do(a) ator(a) que você quer excluir:\n")
        atorDao = AtorDao(conexao)
        atores = atorDao.consultar()

        ator_achado = None
        for ator in atores:
           if int(ator.id) == int(id):
                ator_achado = ator
        
        if ator_achado == None:
            print("Ator(a) não encontrado(a)")
        else:
            atorDao.excluir(ator_achado)
    else:
        print("Essa tabela não existe")

if escolha.upper() == 'E':

    print("Os filmes em ordem alfabética\n")
    filmeDao = FilmeDao(conexao)
    filmes = filmeDao.ordem_alfabetica()
    for filme in filmes:
        print(filme)

if escolha.upper() == 'F':

    print("As médias são:")
    notaDao = NotaDao(conexao)
    notas = notaDao.nota_media()
    for nota in notas:
        print(nota)

if escolha.upper() == 'G':

    print("Os filmes e seus diretores\n")
    filmeDao = FilmeDao(conexao)
    filmes = filmeDao.filme_diretor()
    for filme in filmes:
        print(filme)

if escolha.upper() == 'H':

    texto = input("Digite o nome do diretor:")
    if texto == '':
        print("Nenhum nome digitado")
    else:
        filmeDao = FilmeDao(conexao)
        filmes = filmeDao.buscar_filmes_diretor(texto)
        for filme in filmes:
            print(filme)

conexao.close()