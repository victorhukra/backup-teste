import random

def _gerarCodigo(titulo, ano):
    numeroAno = str(ano) # transofmra ano em string para permitir slicing
    primeiraLetra = titulo[0].upper() # pega a primeira letra do título maiúsculo
    codigoNumero = random.randint(0, 9999) # gera 4 dígitos aleatórios

    if len(numeroAno)>3: # verificações de tamanho apenas para evitar que falte ou sobre dígitos no final de acordo com o tamanho do ano
        return f'{primeiraLetra}{codigoNumero:04d}-{numeroAno[2:]}' 
    elif len(numeroAno)==3: 
        return f'{primeiraLetra}{codigoNumero:04d}-{numeroAno[1:3]}'
    else:
        return f'{primeiraLetra}{codigoNumero:04d}-{ano:02d}'

def cadastrar(acervo): 
    while True:
        try:
            qtdCadastrar = int(input(f'Informe a quantidade de livros que deseja cadastrar: ')) #total de livros que serão cadastrados
            break
        except ValueError:
            print('Informe uma quantidade válida.')

    for i in range(qtdCadastrar): # pede para cada livro seu título, autor, ano e categoria
            
            while True:
                try:
                    titulo = str(input(f'Livro {i+1} - Título: '))
                    if titulo.strip()=='': # evita entradas nulas
                        raise ValueError
                    break
                except ValueError:
                    print('Título não pode ser vazio.')

            while True:
                try:
                    autor = str(input(f'Livro {i+1} - Autor: '))
                    if not autor.replace('.','').replace('-','').replace(' ','').isalpha() or autor.strip()=='': # remove pontos, hífens e espaços para verificar se o nome é válido
                        raise ValueError
                    break
                except ValueError:
                    print('Autor não pode ser vazio ou conter números.')

            while True:
                try:
                    ano = int(input(f'Livro {i+1} - Ano: '))
                    if ano<0 or ano>2025: # valida ano
                        raise ValueError
                    break
                except ValueError:
                    print('Informe um ano válido.')

            while True:
                try:
                    categoria = str(input(f'Livro {i+1} - Categoria: '))
                    if categoria.strip()=='': # evita entradas nulas
                        raise ValueError
                    break
                except ValueError:
                    print('Categoria não pode ser vazia.')

            codigo = _gerarCodigo(titulo, ano) 
            dadosLivros = {'codigo': codigo, 'titulo': titulo, 'autor': autor, 'ano': ano, 'categoria': categoria} #gera dicionário com os valores recebidos
            acervo.append(dadosLivros) #salva no acervo

def listar(acervo): # função que imprime todos os livros presentes no acervo (se houver algum)
    if len(acervo)==0:
        print('\nNão há livros no acervo.')

    for elemento in acervo:
        print(f'{elemento['codigo']} - {elemento['titulo']} | {elemento['autor']} - {elemento['ano']} - {elemento['categoria']}')

        

