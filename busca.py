def buscar(acervo): # definição da função de busca por tipo de informação, seja título, autor ou categoria
    if len(acervo)==0:
        print('\nNão há livros no acervo.')
        return
    
    print('\nMenu de busca:\n1 - Título\n2 - Autor\n3 - Categoria\n')

    while True: # 
        try:
            tipo=int(input('Digite o tipo de busca que deseja realizar: ')) # escolha do tipo de busca que deseja, conforme print indicando menu simples acima
            if tipo<1 or tipo>3:
                raise ValueError
            break
        except ValueError:
            print('Digite um número correspondente.')

    busca=str(input('Digite o que busca: ')) # variável que recebe o que será pesquisado, dependendo do tipo de busca

    encontrado = False
    
    match tipo:
        case 1:
            for livro in acervo: 

                if busca.lower() in livro['titulo'].lower(): # busca por meio do título passando por cada livro no acervo, apresentando as demais informações.
                    encontrado = True
                    print(f'{livro['codigo']} - {livro['titulo']} | {livro['autor']} - {livro['ano']} - {livro['categoria']}')
                    

        case 2:
            for livro in acervo: # busca por meio do autor passando por cada livro no acervo, apresentando as demais informações.
                if busca.lower() == livro['autor'].lower():
                    encontrado = True
                    print(f'{livro['codigo']} - {livro['titulo']} | {livro['autor']} - {livro['ano']} - {livro['categoria']}')
                    
                 
        case 3: 
            for livro in acervo: # busca por meio da categoria passando por cada livro no acervo, apresentando as demais informações.
                if busca.lower() == livro['categoria'].lower():
                    encontrado = True
                    print(f'{livro['codigo']} - {livro['titulo']} | {livro['autor']} - {livro['ano']} - {livro['categoria']}')
    
    if not encontrado: # se nenhum resultado for encontrado
        print('Nenhum livro encontrado.')



