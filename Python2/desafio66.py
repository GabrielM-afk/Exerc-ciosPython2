soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')

# quant = soma = 0
# num = int(input('Digite um número (999 para parar): '))

# while num != 999:
#     soma += num
#     quant += 1
#     num = int(input('Digite um número (999 para parar): '))
# print(f'Foram digitados um total de {quant} números e a soma deles é {soma}!')