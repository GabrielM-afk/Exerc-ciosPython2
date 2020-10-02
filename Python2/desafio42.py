print('-=-' * 8)
print('Análise de Triângulos')
print('-=-' * 8)

r1 = float(input('Digite o comprimento da primeira medida: '))
r2 = float(input('Digite o comprimento da segunda medida: '))
r3 = float(input('Digite o comprimento da terceira medida: '))



print('Os seguimentos acima ', end='')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('formam um triângulo Equilátero')

    elif r1 != r2 == r3 or r1 == r2 != r3 or r1 == r3 != r2:
        print('formam um triângulo Isósceles')

    elif r1 != r2 != r3 != r1:
        print('formam um triângulo Escaleno')

else:
    print('não formam um triângulo')