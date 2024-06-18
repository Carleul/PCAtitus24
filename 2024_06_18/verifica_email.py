def verifica_email(email):
    valida_email = []
    conta_arroba = []
    for letter in email:
        valida_email.append(letter)
        if letter == '@':
            conta_arroba.append('@')
    if len(valida_email) < 3:
        return False
    if valida_email[-4] != '.' or valida_email[-3] != 'c' or valida_email[-2] != 'o' or valida_email[-1] != 'm':
        return False
    elif '@' not in email:
        return False
    if len(conta_arroba) > 1:
        return False
    return True

print(verifica_email('') == False)
print(verifica_email('@') == False)
print(verifica_email('@@') == False)
print(verifica_email('abc@@abc.com') == False)
print(verifica_email('abc@abc.edu') == False)

print(verifica_email('abc@abc.com') == True)
print(verifica_email('a23@123.com') == True)
print(verifica_email('a_b_c@a_b_c.com') == True)
print(verifica_email('a_b_c@a_b_c.com') == True)