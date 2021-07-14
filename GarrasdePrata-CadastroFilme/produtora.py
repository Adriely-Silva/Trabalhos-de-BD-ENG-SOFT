class Produtora:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def to_string(self):
        return 'Id: {} | Nome: {} '.format(self.id, self.nome)