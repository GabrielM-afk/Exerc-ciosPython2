from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>>>>> Qual vai ser a sua opção? '))

    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2

        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente Novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre !')


# import time
# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))

# menu = int(input('-=' * 12 + '''
# [ 1 ] Somar
# [ 2 ] Multiplica
# [ 3 ] Maior
# [ 4 ] Novos números
# [ 5 ] Sair do Programa
# \nO que vc quer fazer ?
# '''))

# time.sleep(1.5)

# while menu != 5:
#     if menu == 1:
#         s = n1 + n2
#         print(f'A soma entre {n1} + {n2} é {s}')
    
#     if menu == 2:
#         m = n1 * n2
#         print(f'A multiplicação entre {n1} + {n2} {m}')

#     if menu == 3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print(f'O maior número digitado entre {n1} e {n2} o maior foi {maior}')

#     if menu == 4:
#         n1 = int(input('Digite o primeiro número: '))

#         n2 = int(input('Digite o segundo número: '))

#         print(f'Os novos números digitados foram {n1} e {n2}')


#     time.sleep(1.5)
#     menu = int(input('-=' * 12 + '''
# [ 1 ] Somar
# [ 2 ] Multiplica
# [ 3 ] Maior
# [ 4 ] Novos números
# [ 5 ] Sair do programa
# \nO que vc quer fazer ?
# '''))

#     time.sleep(1.5)
# print('-=' * 12 + '\nFim do programa... Volte Sempre')
# print('Encerrando..')