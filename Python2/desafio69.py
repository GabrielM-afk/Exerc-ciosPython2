totmulher20 = maioridade = idade18 = 0
sair = False

print('-' * 23)
print('CADASTRE UMA PESSOA')
print('-' * 23)

while sair == False:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M / F] ')).strip().lower
    print('-' * 23)
    sair = str(input('Quer continuar? [S/N]. ')).strip().lower()

    if sexo == 'f' and idade > 20:
        totmulher20 += 1

    if 'n' in sair:
        sair == True 

    elif 's' in sair:
        sair == False

    print('-' * 23)
    print('  CADASTRE UMA PESSOA')
    print('-' * 23)

print(totmulher20)
print('Acabou')
     
