import random

def _gerarCodigo(titulo, ano):
    numeroAno = str(ano)
    primeiraLetra = titulo[0].upper()
    codigoNumero = random.randint(0, 9999)

    if len(numeroAno)>3:
        return f'{primeiraLetra}{codigoNumero:04d}-{numeroAno[2:]}' 
    elif len(numeroAno)==3: 
        return f'{primeiraLetra}{codigoNumero:04d}-{numeroAno[1:3]}'
    else:
        return f'{primeiraLetra}{codigoNumero:04d}-{ano:02d}'

def cadastrar(acervo): 
    while True:
        try:
            qtdCadastrar = int(input(f'Informe a quantidade de livros que deseja cadastrar: '))
            break
        except ValueError:
            print('Informe uma quantidade válida.')

    for i in range(qtdCadastrar):
            
            while True:
                try:
                    titulo = str(input(f'Livro {i+1} - Título: '))
                    if titulo.strip()=='':
                        raise ValueError
                    break
                except ValueError:
                    print('Título não pode ser vazio.')

            while True:
                try:
                    autor = str(input(f'Livro {i+1} - Autor: '))
                    if not autor.replace(' ','').isalpha() or autor.strip()=='':
                        raise ValueError
                    break
                except ValueError:
                    print('Autor não pode ser vazio ou conter números.')

            while True:
                try:
                    ano = int(input(f'Livro {i+1} - Ano: '))
                    if ano<0 or ano>2025:
                        raise ValueError
                    break
                except ValueError:
                    print('Informe um ano válido.')

            while True:
                try:
                    categoria = str(input(f'Livro {i+1} - Categoria: '))
                    if categoria.strip()=='':
                        raise ValueError
                    break
                except ValueError:
                    print('Categoria não pode ser vazia.')

            codigo = _gerarCodigo(titulo, ano)
            dadosLivros = {'codigo': codigo, 'titulo': titulo, 'autor': autor, 'ano': ano, 'categoria': categoria}
            acervo.append(dadosLivros)

def listar(acervo):
    if len(acervo)==0:
        print('\nNão há livros no acervo.')

    for elemento in acervo:
        print(f'{elemento['titulo']} - {elemento['codigo']} | {elemento['autor']} - {elemento['ano']} - {elemento['categoria']}')
        