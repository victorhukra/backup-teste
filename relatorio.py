def escolherRelatorio(conj,acervo,listaAvaliacao):
    if len(acervo)==0:
        print('\nNão há livros no acervo.')
        return
    
    while True: # loop para escolher entre o geral ou o rápido
        print('\n1 - Relatório geral\n2 - Relatório rápido\n')
        try:
            opcao=int(input('Digite uma opção: '))

            if opcao<1 or opcao>2:
                raise IndexError # fora das opções disponíveis
            
            break

        except IndexError:
            print('Digite um número correspondente.')

        except ValueError:
            print('Digite valor válido.')

    match opcao: # escolhe de acordo com a opção
        case 1:
            _gerarRelatorioGeral(conj,acervo,listaAvaliacao)
        case 2:
            _gerarRelatorioRapido(acervo)

def _calcularMediaAvaliacoes(listaAvaliacao):
    avaliacoes={} # dicionário com o código do livros avaliado, soma de todas as suas avaliações e quantidade de avaliações daquele livro específico
    medias={} # dicionário com o código do livro e sua média de avaliações

    for avaliacao in listaAvaliacao: # pra cada avaliação na lista recebida, verifica se o código do livro já existe no dicionário avalições, se não ele gera um novo valor usando o código como chave para os valores da soma e total das suas avaliações
        if avaliacao['codigo'] not in avaliacoes:
            avaliacoes[avaliacao['codigo']] = [0,0]

        avaliacoes[avaliacao['codigo']][0]+=avaliacao['avaliacao'] # altera a soma das avalições
        avaliacoes[avaliacao['codigo']][1]+=1 # aumenta o total de avaliações em mais um

    for elemento in avaliacoes:
        media=avaliacoes[elemento][0]/avaliacoes[elemento][1] #efetua o cálculo da média
        medias[elemento] = media

    return medias # retorna o dicionário com os códigos e suas respectivas médias

def _gerarRelatorioGeral(conj,acervo,listaAvaliacao):

    listaMedia=_calcularMediaAvaliacoes(listaAvaliacao)

    totalLivros = len(acervo)
    totalEmprestados = len(conj)
    totalDisponiveis = totalLivros - totalEmprestados

    categoriasLista = [] #lista de dicionários com cada categoria como chave e uma lista de todos os livros com aquela categoria como valor

    for livro in acervo: # pra cada livro no acervo verifica se sua categoria já existe na lista, caso existe apenas adiciona o livro na lista, caso contrário cria um novo dicionário com a categoria e sua lista de livros correspondentes
        categoriaAtual = livro['categoria']
        encontrado = False

        # verificacao se a categoria ja existe
        for elemento in categoriasLista:
            if elemento['categoria'] == categoriaAtual:
                elemento['livros'].append(livro)
                encontrado = True
                break

        # se nao existe, vai criar no mesmo estilo anterior como uma nova categoria
        if not encontrado:
            novaCategoria = {'categoria': categoriaAtual, 'livros': [livro]}
            categoriasLista.append(novaCategoria)

    with open('relatorio.txt', 'w') as file: # escreve o relatório
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
                file.write(f'- {categoriaNome} ({len(livrosCategoria)}):\n') # imprime cada categoria e o total de livros com aquela respectiva categoria

                for livro in livrosCategoria:
                    if 'titulo' in livro:
                        titulo = livro['titulo']

                    if 'codigo' in livro:
                        codigo = livro['codigo']

                    file.write(f'   - {titulo} ({codigo})\n') # ainda no mesmo loop imprime o título e código de cada livro que pertence a lista daquela categoria
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

                if 'codigo' in livro:
                    codigo = livro['codigo']

                if livro['codigo'] in listaMedia: # verifica se cada livro do acervo tem alguma avaliação
                    media=listaMedia[livro['codigo']]
                else:
                    media='Sem avaliações'

                file.write(f'- {titulo} ({codigo}): {media}\n') # imprime cada livro com sua respectiva média

def _gerarRelatorioRapido(acervo):
    
    with open('relatorio_rapido.txt', 'w') as file: # apenas imprime o título de cada livro presente no acervo
        for livro in acervo:
            if 'titulo' in livro:
                titulo = livro['titulo']

            file.write(titulo + '\n')






