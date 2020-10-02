pn = float(input('Primeiro valor: '))
sn = float(input('Segundo valor: '))

if pn == sn:
    print('Não existe valor maior, os dois são iguais')

elif pn > sn:
    print('O primeiro valor é maior')

elif sn > pn:
    print('O segundo valor é maior')