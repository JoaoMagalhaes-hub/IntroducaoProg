#Lista de contatos
contatos = [

    ['Mãe', '(83) 9 9999-9999', '28/05/1951'],
    ['Polícia', '190', ''],
    ['Samu', '192', ''],
    ['Marcão Lanches (Podrão)', '(83) 9 9898-9898', '18/09/2005'],

]

print(contatos[0][0])

for contato in contatos:
    print(f' Nome: {contato[0]} | Telefone: {contato[1]}') 