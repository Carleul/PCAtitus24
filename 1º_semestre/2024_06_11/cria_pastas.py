import os

pasta = 'pasta_nova'
if not os.path.exists(pasta):
    os.mkdir(pasta)
    print(f"A pasta '{pasta}' foi criada com sucesso.")
else:
    print(f"A pasta '{pasta}' já existe.")