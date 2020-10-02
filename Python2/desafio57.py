sexo = str(input('Informe seu sexo: [M / F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

# import time 
# sexo = str(input('[M / F]: ')).strip().lower()[0]

# while sexo != 'f' and sexo != 'm':
#     print('Digite um sexo válido.')
#     time.sleep(1)
#     sexo = str(input('[M / F]: ')).strip().lower()[0]

# if sexo == 'f':
#     print('Sexo Feminino registrado com sucesso!')

# else:
#     print('Sexo Masculino registrado com sucesso!')
