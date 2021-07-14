import pymysql

from contato import Contato

class ContatoDao:

    def __init__(self):
        self.conexao = pymysql.connect(db = 'ag', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conexao.close()
    
    def inserir(self, contato : Contato):
        self.cursor.execute("INSERT INTO contato (idContato, Nome, Telefone, Endereco, Email, Cidade, Cep, Agenda_idAgenda) VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', {})".format(contato.id, contato.nome, contato.telefone, contato.endereco, contato.email, contato.cidade, contato.cep, contato.id_agenda))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idContato, Nome, Telefone, Endereco, Email, Cidade, Cep, Agenda_idAgenda FROM contato")
        resultados = self.cursor.fetchall()
        contatos = []
        for linha in resultados:
            contatos.append(Contato(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7]))
        return contatos
    
    def atualizar(self, contato : Contato):
        self.cursor.execute("UPDATE contato SET Nome = '{}', Telefone = '{}', Endereco = '{}', Email = '{}', Cidade = '{}', Cep = '{}', Agenda_idAgenda = {} WHERE idContato = {}".format(contato.nome, contato.telefone, contato.endereco, contato.email, contato.cidade, contato.cep, contato.id_agenda, contato.id))
        self.conexao.commit()

    def excluir(self, contato : Contato):
        self.cursor.execute("DELETE FROM contato WHERE idContato = {}".format(contato.id))
        self.conexao.commit()
    
    def buscar_nome(self, nome):
        self.cursor.execute("SELECT idContato, Nome, Telefone, Endereco, Email, Cidade, Cep, Agenda_idAgenda FROM contato WHERE Nome LIKE '%{}%'".format(nome))
        resultados = self.cursor.fetchall()
        contatos = []
        for linha in resultados:
            contatos.append(Contato(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7]))
        return contatos
    
    def buscar_cidade(self, cidade):
        self.cursor.execute("SELECT idContato, Nome, Telefone, Endereco, Email, Cidade, Cep, Agenda_idAgenda FROM contato WHERE Cidade LIKE '%{}%'".format(cidade))
        resultados = self.cursor.fetchall()
        contatos = []
        for linha in resultados:
            contatos.append(Contato(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7]))
        return contatos

    def buscar_cep(self, cep):
        self.cursor.execute("SELECT idContato, Nome, Telefone, Endereco, Email, Cidade, Cep, Agenda_idAgenda FROM contato WHERE Cep LIKE '%{}%'".format(cep))
        resultados = self.cursor.fetchall()
        contatos = []
        for linha in resultados:
            contatos.append(Contato(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7]))
        return contatos
    
    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idContato), 0) + 1 FROM contato")
        resultado = self.cursor.fetchone()
        return int(resultado[0])