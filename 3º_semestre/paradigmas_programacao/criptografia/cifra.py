with open('dicionario.txt','r',encoding='utf-8') as file:
    dicionario = set(file.read().splitlines())

def get_array():
    chars = []
    num = 65
    while True:
        chars.append(chr(num))
        num += 1
        if num > 90:
            break
    especiais = ['.', ',', ';', '!', '?', 'Á', 'Ã', 'À', 'Â', 'É', 'Ê', 'Í', 'Ó', 'Õ', 'Ô', 'Ú', 'Ü', 'Ç']
    for char in especiais:
        chars.append(char)
    return chars
def busca(alfabeto, buscar):
    index = 0
    for char in alfabeto:
        if char == buscar:
            return index
        index=index+1
def solve(frase, alfabeto, cifra):
    resp = ''
    for char in frase:
        if char in alfabeto:
            posicao = busca(alfabeto, char)
            if posicao != -1:
                novo = (posicao + cifra) % len(alfabeto)
                resp += alfabeto[novo]
            else:
                resp += char
        else:
            resp += ' '
    return resp

def nova_frase(frase):
    splitada = frase.split('#')
    nova_frase = ''
    for palavra in splitada:
        nova_frase += f'{palavra} '
    return nova_frase

def tentativa(frase, alfabeto):
    senha = 0
    frases = []
    while senha != 43:
        solved = solve(frase, alfabeto, senha)
        #print(solved + f'Chave: {senha}')
        frases.append(solved)
        senha += 1
    return frases

def verifica(frases):
    contador_max = 0
    frase_definitiva = ''
    chave = 0
    for numero, frase in enumerate(frases):
        frase_splitada = frase.split(' ')
        contador = 0
        for palavra in frase_splitada:
            if palavra.lower() in dicionario:
                contador += 1
        if contador > contador_max:
            contador_max = contador
            frase_definitiva = frase
            chave = numero
    print(f'A frase decifrada é: \n{frase_definitiva} \n A chave é: {chave}')

frase = nova_frase('ÔZÜZ.QÓÇK#CÕ,RI#!Ó,ÕÓAÜÕB#Z#,ÃZC!#ÔZÜZ#;!,ÜÀ?ÜZÜ#Z#?ÜZÇ!#Ç!,Ü!AZ#,ÕÓAÀÓB!#Ç!BÇ#!ÇAB;ÕÇ#!#A!ÓÃZ#ÍBÀAÕ#ÇB,!ÇÇÕKK#')
frases = tentativa(frase, get_array())
verifica(frases)