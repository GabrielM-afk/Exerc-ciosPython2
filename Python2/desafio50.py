s = 0; p = 1

print('=' * 21)
print('10 termos de uma PA')
print('=' * 21)

for n in range(0, 6):
    n = int(input(f'Digite o {p}º número: '))
    p += 1  
    if n % 2 == 0:
        s += n

print(f'O resultado da soma dos números pares foi {s}')