frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print(junto, [inverso])
print('O inverso de {} é {} '.format(junto, inverso))
if inverso == junto:
    print('Ele é um PALÍNDROMO !!')
else:
    print('A frase digitada não é um PALÍNDROMO !!')

# ******************** Minha Versão ************************
# f = input('Digite uma frase: \n').replace(" ", "").upper()

# if f == f[::-1]:
#     print('É um palíndromo')

# else:
#     print('Não é um palíndromo')