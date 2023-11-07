with open('./mobydick.txt',   'r', encoding='utf-8') as livro:
    conteudo = livro.read()
    linhas = livro.readlines()
    qtd_linhas = len(linhas)

    print(conteudo)
    print('-----------------------')
    print(f'Foram impressas {len(linhas)} linhas.')
