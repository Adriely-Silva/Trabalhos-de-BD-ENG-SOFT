class Diretor:

    def __init__(self, id, nome, data_nascimento):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento

    def to_string(self):
        return 'Id: {} | Nome: {} | Data de Nascimento: {}'.format(self.id, self.nome, self.data_nascimento)