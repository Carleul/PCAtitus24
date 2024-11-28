class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - {self.preco:.2f}"

    def __eq__(self, outro):
        return self.preco == outro.preco and self.nome.lower() == outro.nome.lower()