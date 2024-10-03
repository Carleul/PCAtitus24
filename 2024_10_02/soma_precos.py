class Produto:
    def __init__(self, nome: str, custo: float):
        self.nome = nome
        self.custo = custo

    def __add__(self, other):
        if isinstance(other, Produto):
            return self.custo + other.custo
        return 'não foi possível somar os preços'

pizza = Produto('Pizza', 49)
refri = Produto('Refri', 8)
print(pizza + refri)  # 57