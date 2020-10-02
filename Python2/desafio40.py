n1 = float(input('Qual foi a primeira nota ? '))
n2 = float(input('Qual foi a segunda nota ? '))

m = (n1 + n2) / 2

print(f'Tirando {m} você está')

if m <= 5:
    print('Reprovado, tente de novo uma outra hora...')

elif  5 < m <= 6.9:
    print('em Recuperação, estude mais para a próxima prova..')

elif m >= 7:
    print('Aprovado, parabéns')
