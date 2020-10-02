from datetime import date 
ano = date.today().year
totmaior = 0; totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano {}º pessoa nasceu ? \n'.format(pess)))
    idade = ano - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao total tivemos {totmaior} pessoas maiores de idade')
print(f'E total tivemos {totmenor} pessoas menores de idade')

# r = 0; n = 1; a = 0; mn = 0; mr = 0

# for r in range(0, 7):

#     nasc = int(input(f'{n}º Em que ano vc nasceu? \n'))

#     idade = ano - nasc

#     if idade < 18 :
#         mn += 1
    
#     elif nasc >= 18:
#         mr += 1

#     n += 1
    
# if mr > 1 :
#     print(f'Tem {mr} maiores de idade', end='')
#     if mn > 1:
#         print(f' e {mn} menores de idade')
# else:
#     print(f'Tem {mr} maior de idade', end='')
#     print(f' e {mn} menor de idade')