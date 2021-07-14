from nota import Nota

class NotaDao:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def inserir(self, nota : Nota):
        self.cursor.execute("INSERT INTO nota (idNota, Nota, Filme_idFilme) VALUES ({}, {}, {})".format(nota.id, nota.nota, nota.id_filme))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idNota, Nota, Filme_idFilme FROM nota")
        resultados = self.cursor.fetchall()
        notas = []
        for linha in resultados:
            notas.append(Nota(linha[0], linha[1], linha[2]))
        return notas
    
    def atualizar(self, nota : Nota):
        self.cursor.execute("UPDATE nota SET Nota = {}, Filme_idFilme = {} WHERE idNota = {}".format(nota.nota, nota.id_filme, nota.id))
        self.conexao.commit()

    def excluir(self, nota : Nota):
        self.cursor.execute("DELETE FROM nota WHERE idNota = {}".format(nota.id))
        self.conexao.commit()
    
    def nota_media(self):
        self.cursor.execute("SELECT AVG(nota), Filme_idFilme FROM nota GROUP BY Filme_idFilme")
        resultados = self.cursor.fetchall()
        notas = []
        for linha in resultados:
            notas.append({linha[0], linha[1]})
        return notas