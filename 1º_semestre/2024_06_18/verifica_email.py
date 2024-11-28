def verifica_email(email):
    valida_email = []
    for letter in email:
        valida_email.append(letter)
        if letter.isupper():
            return False
    if len(valida_email) < 3:
        return False
    if not email.endswith('.com'):
        return False
    if email.count('.com') != 1:
        return False
    if email.count('@') != 1:
        return False
    return True

print(verifica_email('') == False)
print(verifica_email('@') == False)
print(verifica_email('@@') == False)
print(verifica_email('abc@@abc.com') == False)
print(verifica_email('abc@abc.edu') == False)
print(verifica_email('ABC@abc.edu') == False)

print(verifica_email('abc@abc.com') == True)
print(verifica_email('a23@123.com') == True)
print(verifica_email('a_b_c@a_b_c.com') == True)
print(verifica_email('a_b_c@a_b_c.com') == True)