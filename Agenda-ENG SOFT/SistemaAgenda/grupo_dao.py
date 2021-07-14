import pymysql

from grupo import Grupo

class GrupoDao:

    def __init__(self):
        self.conexao = pymysql.connect(db = 'ag', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conexao.close()
    
    def inserir(self, grupo : Grupo):
        self.cursor.execute("INSERT INTO grupo (idGrupo, Nome) VALUES ({}, '{}')".format(grupo.id, grupo.nome))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idGrupo, Nome FROM grupo")
        resultados = self.cursor.fetchall()
        grupos = []
        for linha in resultados:
            grupos.append(Grupo(linha[0], linha[1]))
        return grupos
    
    def atualizar(self, grupo : Grupo):
        self.cursor.execute("UPDATE grupo SET Nome = '{}' WHERE idGrupo = {}".format(grupo.nome, grupo.id))
        self.conexao.commit()

    def excluir(self, grupo : Grupo):
        self.cursor.execute("DELETE FROM grupo WHERE idGrupo = {}".format(grupo.id))
        self.conexao.commit()
    
    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idGrupo), 0) + 1 FROM grupo")
        resultado = self.cursor.fetchone()
        return int(resultado[0])