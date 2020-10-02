casa = float(input('\nQuanto custa a casa? \n'))
s = float(input('\nQual é o seu salário mensal ?\n'))
anos = int(input('\nEm quantos anos você irá parcelar a casa ? \n'))

prestação = casa / (anos * 12)  

mínimo = s * 30 / 100

if prestação <= mínimo:
    print('Para pagar um casa de R$ {:.2f} em {} anos'.format(casa, anos, end = ' '))
    print('a prestação será de R$ {:.2f}'.format(prestação))
    print('Empréstimo feito')

else:
    print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa, anos, prestação))
    print('Empréstimo Negado')