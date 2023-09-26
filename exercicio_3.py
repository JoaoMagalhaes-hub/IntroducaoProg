import random
from random import randint
numero_clients = 1000
lista_de_respostas= []

while numero_clients > 0:
    lista_de_respostas.append(radint(1, 5))
    numero_clients -= 1

respostas_1 = lista_de_respostas.count(1)
respostas_2 = lista_de_respostas.count(2)
respostas_3 = lista_de_respostas.count(3)
respostas_4 = lista_de_respostas.count(4)
respostas_5 = lista_de_respostas.count(5)

print(f'Quantidade de Respostas 1: {respostas_1} ')
print(f'Quantidade de Respostas 2: {respostas_2}')
print(f'Quantidade de Respostas 3: {respostas_3}')
print(f'Quantidade de Respostas 4: {respostas_4}')
print(f'Quantidade de Respostas 5: {respostas_5}')