from datetime import date
hj = date.today().year

nasc = int(input('Em que ano você nasceu ? '))

idade = hj - nasc

if idade <= 9:
    print('Sua categoria é Mirim')

elif 9 < idade <= 14:
    print('Sua categoria é Infantil')

elif 14 < idade <= 19:
    print('Sua categoria é junior')

elif 19 < idade <= 20:
    print('Sua categoria é sênior')

elif 20 < idade:
    print('Sua categoria é Master') 