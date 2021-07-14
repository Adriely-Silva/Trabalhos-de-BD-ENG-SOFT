import pymysql

from agenda import Agenda

class AgendaDao:
    
    def __init__(self):
        self.conexao = pymysql.connect(db = 'ag', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.cursor.close()
        self.conexao.close()

    def inserir(self, agenda : Agenda):
        self.cursor.execute("INSERT INTO agenda (idAgenda, Nome, Conta_idConta) VALUES ({}, '{}', {})".format(agenda.id, agenda.nome, agenda.id_conta))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idAgenda, Nome, Conta_idConta FROM agenda")
        resultados = self.cursor.fetchall()
        agendas = []
        for linha in resultados:
            agendas.append(Agenda(linha[0], linha[1], linha[2]))
        return agendas
    
    def atualizar(self, agenda : Agenda):
        self.cursor.execute("UPDATE agenda SET Nome = '{}', Conta_idConta = {} WHERE idAgenda = {}".format(agenda.nome, agenda.id_conta, agenda.id))
        self.conexao.commit()

    def excluir(self, agenda : Agenda):
        self.cursor.execute("DELETE FROM agenda WHERE idAgenda = {}".format(agenda.id))
        self.conexao.commit()

    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idAgenda), 0) + 1 FROM agenda")
        resultado = self.cursor.fetchone()
        return int(resultado[0])