import time
peso = float(input('Quantos Quilos você pesa? (kg) '))

altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2 )

print('Seu resultado é....')
time.sleep(1.5)

if imc < 18.5:
    print('\nAbaixo do peso')

elif 18.5 < imc < 25:
    print('\nPeso ideal')

elif 25 < imc < 30:
    print('\nSobrepeso')

elif 30 < imc < 40:
    print('\nObesidade')

elif 40 < imc:
    print('\nObesidade Mórbida') 

time.sleep(1)

print('\nSeu imc é de {:.1f}'.format(imc))