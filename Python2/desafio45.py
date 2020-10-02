from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
time.sleep(1)
print('Ken')
time.sleep(1)
print('PO!!')
time.sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

pc = '\n Há eu Venci'
user = '\n Boa usuário'
meio = '\n Empatou, vamos de novo'

if computador == 0: #pedra
    if jogador == 0:
        print(meio)
    elif jogador == 1:
        print(user)
    elif jogador == 2:
        print(pc)
    else:
        print('Opção inválida')

elif computador == 1: #papel
    if jogador == 0:
        print(pc)
    elif jogador == 1:
        print(meio)
    elif jogador == 2:
        print(user)
    else:
        print('Opção inválida')
elif computador == 2: #tesoura
    if jogador == 0:
        print(user)
    elif jogador == 1:
        print(pc)
    elif jogador == 2:
        print(meio)
    else:
        print('Opção inválida')    

# mao = str(input('''Faça sua escolha: ''')).strip().lower()

# print('Jo... Ken... Pôô..')
# time.sleep(1.5)

# e = ['Pedra', 'Papel', 'Tesoura']

# escolha = random.choice(e)

# pc = '\nHá, eu venci'
# user = '\nBoa usuário'

# if mao == 'pe' or mao == 'p' or mao == 't' or mao == 'pedra' or mao == 'papel' or mao == 'tesoura':

#     if mao == escolha:
#         print('Escolhemos o mesmo, vamos jogar outra vez..')

#     elif mao == 'tesoura' or mao == 't' and escolha == 'Papel':
#         print(user)

#     elif escolha == 'Tesoura' and mao == 'papel' or mao == 'p':
#         print(pc)

#     elif mao == 'pedra' or mao == 'pe' and escolha == 'Tesoura':
#         print(user)

#     elif escolha == 'Pedra' and mao == 'tesoura' or mao == 't':
#         print(pc)

#     elif mao == 'papel' or mao == 'p' and escolha == 'Pedra':
#         print(user)

#     elif escolha == 'pedra' and mao == 'Papel' or mao == 'p' :
#         print(pc)

#     else:
#         print('Opção inválida, tente novamente outra hora.')

#     time.sleep(2)

#     print(f'\nEu escolhi {escolha}')

# else:
#     print('Opção inválida, tente de novo outra hora.')

