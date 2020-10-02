n = int(input('Digite um número para calcular seu fatorial: '))
c = n; f = 1
print(f'Calculando {n}! = ', end='')

for c in range( n, n-1):
    
    f *= c
    c -= 1

print(f) 
    
# while c > 0:
#     print(f'{c} ', end='')
#     print('x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print(f'{f}')