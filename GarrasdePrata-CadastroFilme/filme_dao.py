from filme import Filme

class FilmeDao:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def inserir(self, filme : Filme):
        self.cursor.execute("INSERT INTO filme (idFilme, Titulo, Genero, Ano, ClassificacaoIndicativa, Duracao, Diretor_idDiretor) VALUES ({}, '{}', '{}', '{}', '{}', '{}', {})".format(filme.id, filme.titulo, filme.genero, filme.ano, filme.classificacao_indicativa, filme.duracao, filme.id_diretor))
        self.conexao.commit()

    def consultar(self):
        self.cursor.execute("SELECT idFilme, Titulo, Genero, Ano, ClassificacaoIndicativa, Duracao, Diretor_idDiretor FROM filme")
        resultados = self.cursor.fetchall()
        filmes = []
        for linha in resultados:
            filmes.append(Filme(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]))
        return filmes

    def atualizar(self, filme : Filme):
        self.cursor.execute("UPDATE filme SET Titulo = '{}', Genero = '{}', Ano = '{}', ClassificacaoIndicativa = '{}', Duracao = '{}', Diretor_idDiretor = {} WHERE idFilme = {}".format(filme.titulo, filme.genero, filme.ano, filme.classificacao_indicativa, filme.duracao, filme.id_diretor, filme.id))
        self.conexao.commit()

    def excluir(self, filme : Filme):
        self.cursor.execute("DELETE FROM filme WHERE idFilme = {}".format(filme.id))
        self.conexao.commit()
    
    def ordem_alfabetica(self):
        self.cursor.execute("SELECT f.Titulo FROM filme AS f ORDER BY f.Titulo ASC")
        resultados = self.cursor.fetchall()
        filmes = []
        for linha in resultados:
            filmes.append(linha[0])
        return filmes
    
    def filme_diretor(self):
        self.cursor.execute("SELECT f.Titulo, d.Nome FROM filme AS f JOIN diretor AS d ON (d.idDiretor = f.Diretor_idDiretor)")
        resultados = self.cursor.fetchall()
        filmes = []
        for linha in resultados:
            filmes.append({linha[0], linha[1]})
        return filmes

    def buscar_filmes_diretor(self, texto):
        self.cursor.execute("SELECT Titulo, Diretor_idDiretor FROM filme WHERE Diretor_idDiretor IN(SELECT idDiretor FROM diretor WHERE Nome like '%{}%')".format(texto))
        resultados = self.cursor.fetchall()
        filmes = []
        for linha in resultados:
            filmes.append({linha[0], linha[1]})
        return filmes