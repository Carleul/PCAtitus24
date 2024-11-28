from abc import ABC, abstractmethod


class Produto(ABC):

    @abstractmethod
    def custo_total(self):
        """mostra o custo total do produto."""

    def mostrar_detalhes(self):
        return f'o custo total é de R${self.custo_total():.2f}'

class Pizza(Produto):
    def __init__(self, massa, recheio):
        self.massa = massa
        self.recheio = recheio
        
    def custo_total(self):
        valor = self.massa + self.recheio
        return valor


class Sushi(Produto):
    def __init__(self, arroz, peixe):
        self.arroz = arroz
        self.peixe = peixe

    def custo_total(self):
        valor = self.arroz + self.peixe
        return valor

class Soma:
    @staticmethod
    def soma_tudo(lista_produtos):
        soma = 0
        for produto in lista_produtos:
            soma += produto.custo_total()
        return soma

pizza1 = Pizza(15, 30)
pizza2 = Pizza(12, 40)
sushi1 = Sushi(20, 40)
sushi2 = Sushi(20, 35)

print(pizza1.mostrar_detalhes())
print(sushi1.mostrar_detalhes())
print(f'preço total da compra = R${Soma.soma_tudo([pizza1, pizza2, sushi1, sushi2]):.2f}')