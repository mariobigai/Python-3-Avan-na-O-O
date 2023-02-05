class Funcionario:

    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

jose = Junior('Jose')
print(jose)

luan = Pleno('Luan')
print(luan)

## Entendendo o Mixin
## Luan tem o print definido pelo método __string__ que é herança de HIPSTER
## José não tem o print definido, portanto quando imprimimos o objeto retorna o endereço da memória

## Os mixins são usados desta forma pois o seu comportamento normalmente não precisa ser de responsabilidade da classe filha, pois esta é mais específica.