def verifica_anagramas(str1, str2):
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char in str2:
            continue
        return False

    return True

if verifica_anagramas('anagrama', 'amagrana'):
    print('é um anagrama')
else:
    print('não é um anagrama')