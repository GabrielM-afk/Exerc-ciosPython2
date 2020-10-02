tab = 0; quant = 1

num  = int(input('Quer ver a tabuada de qual valor? '))


print('-' * 12)

while True:
    tab = num * quant
    print(f'{num} x {quant} = {tab}')
    quant += 1
    if quant == 11:
        opção = int(input('Quer ver a tabuada de qual valor? '))
        if num < 0:
            break
        else:
            while True:
                tab = num * quant
                print(f'{num} x {quant} = {tab}')
                quant += 1