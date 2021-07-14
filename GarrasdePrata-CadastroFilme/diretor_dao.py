from diretor import Diretor

class DiretorDao:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def inserir(self, diretor : Diretor):
        self.cursor.execute("INSERT INTO diretor (idDiretor, Nome, DataNascimento) VALUES ({}, '{}', '{}')".format(diretor.id, diretor.nome, diretor.data_nascimento))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idDiretor, Nome, DataNascimento FROM diretor")
        resultados = self.cursor.fetchall()
        diretores = []
        for linha in resultados:
            diretores.append(Diretor(linha[0], linha[1], linha[2]))
        return diretores
    
    def atualizar(self, diretor : Diretor):
        self.cursor.execute("UPDATE diretor SET Nome = '{}', DataNascimento = '{}' WHERE idDiretor = {}".format(diretor.nome, diretor.data_nascimento, diretor.id))
        self.conexao.commit()

    def excluir(self, diretor : Diretor):
        self.cursor.execute("DELETE FROM diretor WHERE idDiretor = {}".format(diretor.id))
        self.conexao.commit()