print('=' * 30)
print('{:^30}'.format('BANCO DO POLVO'))
print('=' * 30)
valor = int(input('Quanto você quer sacar? '))
total = valor
céd = 50
totalCéd = 0
while True:
    if total >= céd:
        total -= céd
        totalCéd += 1
    else: 
        if totalCéd > 0:
            print(f'Total de {totalCéd} em cédulas de R$ {céd}')
        
            if céd == 50:
                céd = 20
            
            if céd == 20:
                céd = 10
            
            if céd == 10:
                céd = 1
            
            totalCéd = 0
            if total == 0:  
                break

print('=' * 30)
print('Volte sempre ao Banco do Polvo!')