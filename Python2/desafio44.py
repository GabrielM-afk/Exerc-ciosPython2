print('{:=^40}'.format(' Casa Do sono '))
pn = float(input('Preço das compras: R$ '))
cp = str(input('''Qual é a condição de pagamento ? 
    [ 1 ] à vista Diheiro/ cheque 
    [ 2 ] 1x no cartão 
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão
    Qual vai ser a opção ? ''')).strip().lower()

if cp == '1':
    v = pn - pn * 10 / 100

elif cp == '2':
    v = pn - pn * 5 / 100

elif cp == '3':
    v = pn

elif cp == '4':
    v = pn + pn * 20 / 100
    
else:
    print('Opção inválida, tente novamente !')    
print('O preço do produto será de R$ {:.2f}'.format(v))