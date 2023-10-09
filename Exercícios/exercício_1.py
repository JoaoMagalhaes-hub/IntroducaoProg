compra = float(input(' Digite o valor total da sua compra: '))
if compra > 100:
    compra -= (compra * 0.1)
    print(f' Você recebeu um desconto de 10%, a sua compra saiu em um total de {compra}!')
elif compra < 101 and compra > 49:
    compra -= (compra * 0.05)
    print(f' Você recebeu um desconto de 5%, a sua compra saiu em um total de {compra}!')
elif compra < 50: 
    compra = compra
    print(f'Você não receberá nenhum desconto, a sua compra saiu em um total de {compra} :(')