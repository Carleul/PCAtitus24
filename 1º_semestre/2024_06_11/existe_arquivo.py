import os
def retorna_conteudo(meu_arquivo: str) -> str:
    if os.path.exists(meu_arquivo):
        file = open(meu_arquivo, 'r')
        conteudo = file.read()
        file.close()
        return conteudo
    else:
        return 'arquivo não existe'

print(retorna_conteudo('meu_arquivo2.txt'))