from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi? ')
acertou = False; palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')

        elif computador < jogador:
            print('Menos... Tente mais uma vez.')
        
print('Acertou com {} tentativas. Parabéns !'.format(palpites))

# import random, time
# t = 0; n = random.randint(0, 10)

# print('-=-' * 10)
# print('Estou pensando em um número...')
# print('-=-' * 10)
# time.sleep(1)
# nu = int(input('Tente adivinhar no número em que pensei: '))

# print('\n processando...\n')
# time.sleep(2)

# while n != nu:

#     if nu > n:
#         print('Menos.. tenta de novo')
    
#     elif n > nu:
#         print('Mais.. Tenta de novo')
#     t += 1

#     nu = int(input('\n  Tente adivinhar no número em que pensei: '))

#     print('Processando..')
#     time.sleep(2)

# print('\n  Boa, a próxima vai ser mais difícil')
# print(f'Mas vc teve que tentar {t} vezes até conseguir')