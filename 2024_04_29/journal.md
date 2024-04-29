# Anotações 29/04

- Operações:
  - split()
    - divide uma string em uma lista de strings separadas pelo elemento evidenciado no comando
  - slice - string[0]
    -  fatia a string de acordo com o item informado
    - [start:stop:step]
      - não entendi direito como funciona
  - join
    - adiciona elementos entre os itens da lista
    - ex: lista = ['um', 'dois', 'tres']
          print(', '.join(lista))
          >>> um, dois, tres
  - replace
    - substitui itens
    - frase = 'eu gosto de One Piece'
    - print(frase.replace('One Piece', 'Fate'))
    >>> eu gosto de Fate
  - find
    - procura por uma substring dentro da string, e diz a posição anterior à primeira letra da substring, e retorna -1 se não achar (lembrando que a primeira posição é zero)
  - upper, lower, e capitalize
    - texto = i Am THe BOnE Of mY SWorD
    - texto_min = texto.lower() - i am the bone of my sword
    - texto_mai = texto.upper() - I AM THE BONE OF MY SWORD
    - texto_cap = texto.capitalize() - I am the bone of my sword