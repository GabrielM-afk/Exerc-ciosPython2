from datetime import date

hj = date.today().year

nasc = int(input('Em que ano vc nasceu ? '))

idade = hj - nasc

if idade == 18:
    print('Vc deve se alistar, agora')

elif idade < 18:
    r = 18 - idade
    print(f'Vai demora {r} anos para vc se alistar ainda')
    ano = hj + r
    print(f'Seu alistamento vai ser em {ano}')

elif idade > 18:
    r = idade - 18
    print(f'Vc não precisa se alistar, pois já passou {r} anos')
    ano = hj - r
    print(f'Você deveria ter se alistado no ano {ano}')