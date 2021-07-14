from produtora import Produtora

class ProdutoraDao:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def inserir(self, produtora : Produtora):
        self.cursor.execute("INSERT INTO produtora (idProdutora, Nome) VALUES ({}, '{}')".format(produtora.id, produtora.nome))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idProdutora, Nome FROM produtora")
        resultados = self.cursor.fetchall()
        produtoras = []
        for linha in resultados:
            produtoras.append(Produtora(linha[0], linha[1]))
        return produtoras
    
    def atualizar(self, produtora : Produtora):
        self.cursor.execute("UPDATE produtora SET Nome = '{}' WHERE idProdutora = {}".format(produtora.nome, produtora.id))
        self.conexao.commit()

    def excluir(self, produtora : Produtora):
        self.cursor.execute("DELETE FROM produtora WHERE idProdutora = {}".format(produtora.id))
        self.conexao.commit()