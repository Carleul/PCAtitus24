class A:
    qtd = 0
    def __init__(self, nome):
        self.nome = nome
        A.qtd += 1

class B(A):
    def __init__(self, nome, atributo):
        super().__init__(nome)
        self.atributo = atributo

    def __str__(self):
        return f'{self.nome}, {self.atributo} {A.qtd}'

B1 = B('seiba', 'saber')
B2 = B('sasaki', 'assassin')
print(B1)
print(B2)