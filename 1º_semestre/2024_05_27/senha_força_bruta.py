import zipfile

NOME_ARQUIVO = "senha_bitcoin.zip"
zip_file = zipfile.ZipFile(NOME_ARQUIVO, 'r')


def extrair_arquivo_zip_com_senha(senha):
    try:
        zip_file.extractall(path='.', pwd=senha.encode('utf-8'))
        return True
    except:
        pass
    return False


################################################
# Não alterar linhas acima:
################################################

extraido = False
contador = 0
caracteres_possiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                        'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                        '8', '9']
for char1 in caracteres_possiveis:                                              # nas linhas 28 até trinta
    for char2 in caracteres_possiveis:                                          # estou gerando códigos de
        for char3 in caracteres_possiveis:                                      # 3 caracteres
            if char1.isdigit() or char2.isdigit() or char3.isdigit():           # e nas de 31 até 33
                if char1.isupper() or char2.isupper() or char3.isupper():       # garantindo que serão senhas
                    if char1.islower() or char2.islower() or char3.islower():   # válidas nas regras
                        senha = char1 + char2 + char3
                        contador += 1
                        extraido = extrair_arquivo_zip_com_senha(senha)         # nessa outra parte testo as senhas
                        if extraido:
                            print('senha:', senha)
                            print('senha encontrada com sucesso em', contador, 'tentativas')
                            exit()
for char1 in caracteres_possiveis:
    for char2 in caracteres_possiveis:           # nessa segunda parte o processo
        for char3 in caracteres_possiveis:           # é basicamente o mesmo, mas com
            for char4 in caracteres_possiveis:           # 4 digitos agora se as de 3 não funcionarem
                if char1.isdigit() or char2.isdigit() or char3.isdigit() or char4.isdigit():
                    if char1.isupper() or char2.isupper() or char3.isupper() or char4.isupper():
                        if char1.islower() or char2.islower() or char3.islower() or char4.islower():
                            senha = char1 + char2 + char3 + char4
                            contador += 1
                            extraido = extrair_arquivo_zip_com_senha(senha)
                            if extraido:
                                print('senha:', senha)
                                print('senha encontrada com sucesso em', contador, 'tentativas')
                                exit()