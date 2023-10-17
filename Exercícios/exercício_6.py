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