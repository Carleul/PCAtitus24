ANO_ATUAL = 2025

ano = int(input('qual o seu ano de nascimento?')

if ano > ANO_ATUAL or ano > ANO_ATUAL - 150
        print('cadastro negado.')
        
estudo = input('você estuda? responda com s ou n:')
        
if estudo == 'n'and ano > ANO_ATUAL - 14:
        print('cadastro aprovado com ressalvas.')
        
trabalho = input('você trabalha? responda com s ou n:')

if trabalho == 's':
        regime = input('você é mei, estag ou outro?')

        renda = float(input('qual é o valor da sua renda?')
                
        if renda < 0:
                print('cadastro negado.')
                
        if regime == 'mei' and renda > 6750:
                print('cadastro reprovado.')

        if regime == 'estag' and estudo != 's':
                print('cadastro reprovado.')

        if ano > ANO_ATUAL - 14:
                print('cadastro reprovado.')

        if estudo == 's'and ano >= ANO_ATUAL - 14 and ano <= ANO_ATUAL - 16:
                print('cadastro reprovado.')
elif:
        aposentadoria = input('você é aposentado? responda com s ou n:')

        if aposentadoria == 's'and ano > ANO_ATUAL - 62:
                print('cadastro aprovado.')
else:
        print('cadastro aprovado.')
