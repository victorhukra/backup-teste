def buscar(acervo):
    if len(acervo)==0:
        print('\nNão há livros no acervo.')
        return
    
    print('\nMenu de busca: :\n1 - Título\n2 - Autor\n3 - Categoria\n')

    while True:
        try:
            tipo=int(input('Digite o tipo de busca que deseja realizar: '))
            if tipo<1 or tipo>3:
                raise ValueError
            break
        except ValueError:
            print('Digite um número correspondente')

    busca=str(input('Digite o que busca: '))

    match tipo:
        case 1:
            for livro in acervo:
                if busca.lower() in livro['titulo'].lower():
                    print(f'\nLivro encontrado:',livro['codigo'],livro['titulo'],livro['autor'],livro['ano'],livro['categoria'])
                    return

        case 2:
            for livro in acervo:
                if busca.lower() == livro['autor'].lower():
                    print(f'\nLivro encontrado:',livro['codigo'],livro['titulo'],livro['autor'],livro['ano'],livro['categoria'])
                    return
                 
        case 3: 
            for livro in acervo:
                if busca.lower() == livro['categoria'].lower():
                    print(f'\nLivro encontrado:',livro['codigo'],livro['titulo'],livro['autor'],livro['ano'],livro['categoria'])
                    return
        
    print('Nenhum livro encontrado')

