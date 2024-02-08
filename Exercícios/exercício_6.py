import random
from random import randint

resultado_da_soma = 0
lista = []


for n in range(20):
    lista.append(randint(1 , 10))


for i in lista:
    if (i % 2) == 0:
        resultado_da_soma += i
        
print(f'O resultado da soma é: {resultado_da_soma}')        
print(lista)

# Uniesp - Centro Universitário
# Exercício 1 


# Altura dos homens e o seu gênero
gender_m = (7)
altura_m = [1.86 , 1.99, 1.76, 2.00, 1.55, 1.45, 1.98]

# Altura das mulheres e seu gênero
gender_f = (8)
altura_f = [1.35, 1.67, 1.20, 1.34, 1.76, 1.87, 1.56, 1.58]

# A altura de ambos os gênero
altura_all = [1.86 , 1.99, 1.76, 2.00, 1.55, 1.45, 1.35, 1.67, 1.20, 1.34, 1.76, 1.87, 1.56, 1.58, 1.98]

# A média da altura dos homens 
media_altura_m = sum(altura_m/7)

# A altura maior e menor já selecionada na lista de ambos os gêneros
altura_maior = max(altura_all)
altura_menor = min(altura_all)

print(f'A maior altura do grupo é: {altura_maior} e a menor altura é: {altura_menor}!')
print(f'A média da altura dos homens é: {media_altura_m}!')
print(f'O número de mulheres é :{gender_f}')
