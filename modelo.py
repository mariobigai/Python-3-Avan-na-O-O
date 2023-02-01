class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    def __str__(self):
        return f"Filme: {self.__nome}, Ano: {self.ano}, Duração: {self.duracao}, Likes: {self.__likes}"

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_likes(self):
       self.__likes += 1

    def __str__(self):
        return f"Série: {self.__nome}, Ano: {self.ano}, Temporadas: {self.temporadas}, Likes: {self.__likes}"

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(100*"-")
print(vingadores)
print(100*"-")
print("Teste Likes")
print(f'Antes: {vingadores.likes}')
vingadores.dar_likes()
vingadores.dar_likes()
print(f'Depois: {vingadores.likes}')
print(100*"-")
print("Teste nome")
print(f'Antes:{vingadores.nome}')
vingadores.nome = 'vingadores - aquele que todo mundo briga'
print(f'Depois:{vingadores.nome}')
print(100*"-")
print('\n')

atlanta = Serie('atlanta', 2016, 2)
print(100*"-")
print(atlanta)
print(100*"-")
print("Teste Likes")
print(f'Antes: {atlanta.likes}')
atlanta.dar_likes()
print(f'Depois: {atlanta.likes}')
print(100*"-")
print("Teste nome")
print(f'Antes:{atlanta.nome}')
atlanta.nome = 'atlanta = aquele série do Donal Glover'
print(f'Depois:{atlanta.nome}')
print(100*"-")
