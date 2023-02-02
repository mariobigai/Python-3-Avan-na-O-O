class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie('atlanta', 2016, 2)
atlanta.dar_likes()
atlanta.dar_likes()

lista = [atlanta, vingadores]

for programa in lista:
    detalhe = f'{programa.duracao} min' if hasattr(programa, 'duracao') else f'{programa.temporadas} Temporadas'
    print(f'Nome: {programa.nome} - {detalhe} - Likes: {programa.likes}')
