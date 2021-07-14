class Filme:

    def __init__(self, id, titulo, genero, ano, classificacao_indicativa, duracao, id_diretor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.classificacao_indicativa = classificacao_indicativa
        self.duracao = duracao
        self.id_diretor = id_diretor

    def to_string(self):
        return 'Id: {} | Título: {} | Gênero: {} | Ano: {} | Classificação Indicativa: {} | Duração: {} | Id do(a) Diretor(a): {}'.format(self.id, self.titulo, self.genero, self.ano, self.classificacao_indicativa, self.duracao)