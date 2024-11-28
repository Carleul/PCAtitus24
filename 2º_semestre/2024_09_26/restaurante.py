class Produto:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f'{self.nome} {self.descricao} R$ {self.preco}'

class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.__catalogo = []

    def __str__(self):
        return f'{self.nome}, quantidade de produtos: {self.tamanho_catalogo()}, maior preço: {self.mais_caro()}'

    def encher_catalogo(self, produto):
        return self.__catalogo.append(produto)

    def tamanho_catalogo(self):
        return len(self.__catalogo)

    def mais_caro(self):
        return 

restaurante1 = Restaurante('Larika')
produto1 = Produto('banana', 'amarela', 1.99)
restaurante1.encher_catalogo(produto1)
produto2 = Produto('arroz', 'branco', 15.99)
restaurante1.encher_catalogo(produto2)
produto3 = Produto('maminha', 'mal passada', 64.99)
restaurante1.encher_catalogo(produto3)

print(restaurante1)