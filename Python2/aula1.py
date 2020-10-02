nome = str(input('\n Qual é o seu nome ? \n')).lower().strip()

if nome == 'gabriel':
    print('\n Boa jão')

elif nome == 'maria' or nome == 'pedro':
    print('\n BOAH')

elif nome in 'ana claudia jessica mariana':
    print('Belo nome feminino')

else:
    print('Seu nome é bem normal')

print(f'Bom dia {nome}')