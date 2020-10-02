import random, time
print('Par ou impar, escolha seu lado')

computador = random.randint(0, 15)

jogador = str(input('Faça sua escolha [ Par / Impar ]: ')).strip().lower()

escolha = ['par', 'impar']
 
ganhador = vezes = 0

while jogador != ganhador:

    # IF CHOICE YOUR OPTOIN (IMPAR / PAR) 
    if jogador == escolha[0]:
        num = int(input('Você escolheu par.. Digite um número [ 0 / 15 ]: '))
    
    elif jogador == escolha[1]:
        num = int(input('Você escolheu impar.. Digite um número [ 0 / 15 ]: '))

    vezes += 1
    ganhador = num + computador
    
    # IMPAR
    if jogador == escolha[0]: 

        if ganhador % 2 != 0 :
            ganhador == computador
            print('Logo você verá seu resultado..')
            time.sleep(1.5)
            break

        else:
            ganhador == jogador
            print('Mais uma vez')

    # PAR
    elif jogador == escolha[1]:
        if ganhador % 2 == 0:
            ganhador == jogador
            print('Mais uma vez')

        else:
            ganhador == computador
            print('Logo você verá seu resultado..')
            time.sleep(1.5)
            break

print(f'Parabéns, você perdeu depois de {vezes} tentativas')
print(computador)