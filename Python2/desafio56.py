somaidade = mediaidade = maioridadeHomem = 0;  nomevelho = ''; totmulher20 = 0

for p in range(1, 5):
    print(f'-------- {p}º Pessoa --------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M / F]: ')).strip()
    somaidade += idade 

    if p == 1 and sexo in "Mm":
        maioridadeHomem += idade
        nomevelho = nome
    
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomevelho = nome
        
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1 

mediaidade = somaidade / 4

print('\nA média de idade  do grupo é de {} anos'.format(mediaidade))
print('\nO homem mais velho tem {} anos e se chama {}.'.format(maioridadeHomem, nomevelho))
print(f'\nAo todo são {totmulher20} mulheres com menos de 20 anos')