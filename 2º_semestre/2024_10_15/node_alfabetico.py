from product import Product

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first_node = None

    def __str__(self):
        valores = []
        current = self.first_node
        while current is not None:
            valores.append(str(current.value.nome))
            current = current.next
        return " -> ".join(valores)

    def add(self, value):
        new_node = Node(value)
        if not isinstance(value, Product):
            raise TypeError()
        current = self.first_node
        if current is None or value.nome < current.value.nome:
            new_node.next = current
            self.first_node = new_node
        else:
            while current.next.value.nome < value.nome:
                current = current.next
            new_node.next = current.next
            current.next = new_node


    def remove(self, value):
        current = self.first_node
        anterior = None
        while current is not None:
            if current.value == value:
                if anterior is None:  # Remover o primeiro nó
                    self.first_node = current.next
                else:
                    anterior.next = current.next  # Pular o nó removido
                return  # Termina após a remoção
            anterior = current
            current = current.next
        print(f"Valor {value} não encontrado na lista.")

    def position(self, value):
        current = self.first_node
        result = 0
        while current is not None:
            if current.value == value:
                return result
            current = current.next
            result += 1
        return -1  # Indica que o value não foi encontrado


# Criando uma lista encadeada
lista = LinkedList()

produto1 = Product('banana', 2.99)
produto2 = Product('laranja', 3)
produto3 = Product('abacaxi', 3)

lista.add(produto2)
lista.add(produto1)
lista.add(produto3)

print(lista) # abacaxi -> banana -> laranja