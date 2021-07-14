import pymysql

from grupocontato import GrupoContato

class GrupoContatoDao:

    def __init__(self):
        self.conexao = pymysql.connect(db = 'ag', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conexao.close()
    
    def inserir(self, grupocontato : GrupoContato):
        self.cursor.execute("INSERT INTO grupocontato (Grupo_idGrupo, Contato_idContato) VALUES ({}, {})".format(grupocontato.idgrupo, grupocontato.idcontato))
        self.conexao.commit()
    
    def excluir(self, grupocontato : GrupoContato):
        self.cursor.execute("DELETE FROM grupocontato WHERE Grupo_idGrupo = {} AND Contato_idContato = {}".format(grupocontato.idgrupo, grupocontato.idcontato))
        self.conexao.commit()
    
    def consultar(self, grupocontato : GrupoContato):
        self.cursor.execute("SELECT * FROM grupocontato WHERE Grupo_idGrupo = {} AND Contato_idContato = {}".format(grupocontato.idgrupo, grupocontato.idcontato))
        resultado = self.cursor.fetchone()
        return resultado
