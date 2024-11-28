MAIORIDADE = 18

def verifica_maioridade(idade):
    return idade >= MAIORIDADE

idade = int(input('Digite sua idade: '))
if verifica_maioridade(idade):
    print('você é maior de idade.')
else:
    print('você é menor de idade.')