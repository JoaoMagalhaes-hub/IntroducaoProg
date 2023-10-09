# Criar uma lista com 5 clubes
clubes_de_futebol = [
    'ibis',
    'flamengo',
    'volta redonda',
    'nacional de patos'
]


#Perguntar qual o  clube o usuário vai verificar
clube_pequisado = input('Digite o clube(Escolhe vasco pfvr): ')
for clube in clubes_de_futebol:
    if clube == clube_pequisado:
        print('Achei o teu timão')
    else:
        print('Teu time é mt bom para')