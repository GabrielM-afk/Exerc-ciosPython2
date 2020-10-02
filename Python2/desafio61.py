print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1; total = 0; m = 10
while m != 0:
    total = total + m
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('Pauser')
    m = int(input('Quantos termos vc quer a mais? '))
print(f'Vc terminou a PA com {total} termos')

