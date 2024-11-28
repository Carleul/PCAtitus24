# Anotações 23/04

- hoje eu fui o ajudante da turma :D
- Comando dir
    - o comando dir() é usado para listar as variáveis disponíveis
    - dir(variável) lista os metodos disponíveis na variável
- listas são coleções mutáveis e ordenadas de itens heterogênos
    - itens *heterogêneos* são diferentes tipos(string, inteiro, float, etc.)
- *lembrar que toda lista começa do 0!!*
- Listas:
    - Mutável - pode ser mudada ao longo do código
        - len() - mostra o tamanho da lista, o número de itens - len(lista)
        - append() - adiciona um item à lista na última posição - lista.append('item')
        - remove() - remove o item pedido - lista.remove('item')
        - pop() - remove o último item da lista - lista.pop() remove o último elemento , lista.pop(1) remove o segundo elemento
    - Ordenada
        - lista[0] - mostra o primeiro item da lista
        - lista[-1] - mostra o último item da lista
        - lista[1:4] - mostra os itens do segundo ao quarto. obs: ele inclui o primeiro número do comando mas não o segundo
        - index() - mostra a posição do item - lista.index('terceiro_item') -> 2
        - in -  verifica se algo está na lista - 'item_fora' in lista -> False
    - Heterogênea
        - pode se ter diferentes elementos dentro da lista, inclusive listas dentro de listas
- Tuplas:
    - Imutável - comandos abaixo dão erro no programa
        - append()
        - remove()
        - pop() 
        - tupla[0] = item
    - Ordenada
        - os mesmos comandos das listas podem ser usados
    - Heterogênea
        - as mesmas regras das listas se aplicam

- Laços de Repetição:
    - for
        - Itera por uma lista de itens, executando o mesmo trecho de código para cada elemento.
        - for number in [1, 2, 3, 4, 5]:
        - bloco de comandos
    - range
        - executa um comando pelas vezes que o número representa e altera seu valor de um em um
        - for i in range(5)
        - i = 0
        .
        .
        .
        - i = 5
    - while
        - executa um trecho enquanto a condição for verdadeira
        - while tasks != 0:
    - list comprehension
        - um syntactic sugar do for
        - nova lista = [expressão for elemento in sequencia]
    