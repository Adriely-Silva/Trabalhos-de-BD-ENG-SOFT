import pymysql

from conta import Conta

class ContaDao:

    def __init__(self):
        self.conexao = pymysql.connect(db = 'ag', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conexao.close()
    
    def inserir(self, conta : Conta):
        self.cursor.execute("INSERT INTO conta (idConta, Nome, Email, Senha) VALUES ({}, '{}', '{}', '{}')".format(conta.id, conta.nome, conta.email, conta.senha))
        self.conexao.commit()
    
    def consultar(self):
        self.cursor.execute("SELECT idConta, Nome, Email, Senha FROM conta")
        resultados = self.cursor.fetchall()
        contas = []
        for linha in resultados:
            contas.append(Conta(linha[0], linha[1], linha[2], linha[3]))
        return contas
    
    def atualizar(self, conta : Conta):
        self.cursor.execute("UPDATE conta SET Nome = '{}', Email = '{}', Senha = '{}' WHERE idConta = {}".format(conta.nome, conta.email, conta.senha, conta.id))
        self.conexao.commit()

    def excluir(self, conta : Conta):
        self.cursor.execute("DELETE FROM conta WHERE idConta = {}".format(conta.id))
        self.conexao.commit()
    
    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idConta), 0) + 1 FROM conta")
        resultado = self.cursor.fetchone()
        return int(resultado[0])
    
    def login(self, id, senha):
        self.cursor.execute("SELECT c.idConta, c.Nome, c.Email FROM conta AS c WHERE c.idConta = {} AND c.Senha = '{}'".format(id, senha))
        resultado = self.cursor.fetchone()
        return resultado
