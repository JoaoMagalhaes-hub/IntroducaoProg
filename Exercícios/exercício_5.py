import random
from random import randint

Q = []

for numero in range(20):
    Q.append(randint(1 , 100))

print(Q)

# Variável de controle 
maior = -1
menor = 101
for i in Q:
    if maior < i:
        maior = i 

    if menor > i:
        menor = i

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

print(max(Q))
print(min(Q))