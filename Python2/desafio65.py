resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        
        if num < menor:
            menor = num

    resp = str(input('Quer continua? [S / N]')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi de {média}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')



# n1 = int(input('Digite um número: '))
# opção = 0; m = 0; v = 1; maior = 0; menor = 0


# while opção != 's':

#     n2 = int(input('Digite outro número: '))
#     opção = str(input('Quer parar ?\n')).lower().strip()
    
#     if opção != 0:

#         if n2 > n1:
#             maior = n2
#             menor = n1

#         if n1 > n2:
#             maior = n1
#             menor = n2

#     v += 1

# m = ( n1 + n2 )/ v

# print(f'A média dos números é {m}')
# print(f'O maior número digitado foi {maior}')
# print(f'O menor número digitado foi {menor}')