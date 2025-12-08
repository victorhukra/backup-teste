def escolherRelatorio(conj,acervo):
    if len(acervo)==0:
        print('\nNão há livros no acervo')
        return
    
    while True:
        print('\n1 - Relatório geral\n2 - Relatório rápido\n')
        try:
            opcao=int(input('Digite uma opção: '))

            if opcao<1 or opcao>2:
                raise IndexError
            
            break

        except IndexError:
            print('Digite um número correspondente')

        except ValueError:
            print('Digite valor válido')

    match opcao:
        case 1:
            _gerarRelatorioGeral(conj,acervo)
        case 2:
            _gerarRelatorioRapido(acervo)

def _calcularMediaAvaliacoes(livro):
    '''implementar'''

def _gerarRelatorioGeral(conj,acervo):

    totalLivros = len(acervo)
    totalEmprestados = len(conj)
    totalDisponiveis = totalLivros - totalEmprestados

    categoriasLista = []

    for livro in acervo:
        categoriaAtual = livro['categoria']
        encontrado = False

        #verificacao se a categoria ja existe
        for item in categoriasLista:
            if item['categoria'] == categoriaAtual:
                item['livros'].append(livro)
                encontrado = True
                break

        #se nao existe, vai criar no mesmo estilo anterior como uma nova categoria
        if not encontrado:
            novaCategoria = {
                'categoria': categoriaAtual,
                'livros': [livro]
            }
            categoriasLista.append(novaCategoria)

    with open('relatorio.txt', 'w') as file:
        file.write('RELATÓRIO GERAL DA BIBLIOTECA\n')
        file.write('--------------------------------\n')

        #1. Total de livros
        file.write(f'1. Total de livros cadastrados: {totalLivros}\n\n')

        #2. Livros por categoria
        file.write('2. Livros por categoria:\n')
        if not categoriasLista:
            file.write('Não há livros cadastrados.\n\n')
        else:
            for item in categoriasLista:
                categoriaNome = item['categoria']
                livrosCategoria = item['livros']
                file.write(f'- {categoriaNome} ({len(livrosCategoria)}):\n')

                for livro in livrosCategoria:
                    if 'titulo' in livro:
                        titulo = livro['titulo']
                    else:
                        titulo = 'Sem título'

                    if 'codigo' in livro:
                        codigo = livro['codigo']
                    else:
                        codigo = 'Sem código'

                    file.write(f'   - {titulo} ({codigo})\n')
            file.write('\n')

        #3. Quantidade de livros emprestados e disponíveis
        file.write('3. Situação dos livros:\n')
        file.write(f'- Emprestados: {totalEmprestados}\n')
        file.write(f'- Disponíveis: {totalDisponiveis}\n\n')

        #4. Média das avaliações por livro
        file.write('4. Média das avaliações por livro:\n')
        if not acervo:
            file.write('Não há livros cadastrados para avaliar.\n')
        else:
            for livro in acervo:
                if 'titulo' in livro:
                    titulo = livro['titulo']
                else:
                    titulo = 'Sem título'

                if 'codigo' in livro:
                    codigo = livro['codigo']
                else:
                    codigo = 'Sem código'

                media = _calcularMediaAvaliacoes(livro)
                file.write(f'- {titulo} ({codigo}): {media}\n')

def _gerarRelatorioRapido(acervo):
    
    with open('relatorio_rapido.txt', 'w') as file:
        for livro in acervo:
            if 'titulo' in livro:
                titulo = livro['titulo']
            else:
                titulo = 'Sem título'
            file.write(titulo + '\n')




