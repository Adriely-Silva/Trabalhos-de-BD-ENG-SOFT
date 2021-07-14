class Nota:

    def __init__(self, id, nota, id_filme):
        self.id = id
        self.nota = nota
        self.id_filme = id_filme

    def to_string(self):
        return 'Id: {} | Nota: {} | Id do Filme: {}'.format(self.id, self.nota, self.id_filme)