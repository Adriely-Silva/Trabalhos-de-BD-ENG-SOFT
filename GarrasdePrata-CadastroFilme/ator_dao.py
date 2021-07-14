from ator import Ator

class AtorDao:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()
    
    def inserir(self, ator : Ator):
        self.cursor.execute("INSERT INTO ator (idAtor, Nome, DataNascimento) VALUES ({}, '{}', '{}')".format(ator.id, ator.nome, ator.data_nascimento))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idAtor, Nome, DataNascimento FROM ator")
        resultados = self.cursor.fetchall()
        atores = []
        for linha in resultados:
            atores.append(Ator(linha[0], linha[1], linha[2]))
        return atores
    
    def atualizar(self, ator : Ator):
        self.cursor.execute("UPDATE ator SET Nome = '{}', DataNascimento = '{}' WHERE idAtor = {}".format(ator.nome, ator.data_nascimento, ator.id))
        self.conexao.commit()

    def excluir(self, ator : Ator):
        self.cursor.execute("DELETE FROM ator WHERE idDiretor = {}".format(ator.id))
        self.conexao.commit()