num = cont = soma = 0
num = int(input('Digite um número [digite 999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [digite 999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')



# num = int(input('Digite um número: '))
# cont = 0; n = 0

# while num != 999:
#     cont += 1;  n += num
#     num = int(input('Digite +1 número: '))
   

# print(f'Foram digitados {cont} vezes')
# print(f'A soma deles é {n}')
