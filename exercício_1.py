compra = float(input(' Digite o valor total da sua compra: '))
if compra > 100:
    print('Você recebeu um desconto de 10%!')
elif compra < 101 and compra > 49:
    print(' Você recebeu um desconto de 5%! ')
else:
    print('Você não receberá nenhum desconto :(')