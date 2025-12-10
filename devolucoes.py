from datetime import datetime

def devolucoesEmprestimo(conj,acervo,lista): 
    if len(acervo)==0:
        print('\nNão há livros no acervo.')
        return
    
    devolucao=str(input('\nDigite o título do livro a ser devolvido: '))
    for registro in acervo: 
        
        titulo = registro['titulo']
        codigo = registro['codigo']

        if registro['titulo']==devolucao: # verifica se o título existe no acervo
            codigoDevolucao=registro['codigo']

            if codigoDevolucao in conj: # verifica se o código daquele livro existe no conjunto de emprestados
                with open('emprestimos.txt','r+') as arquivo:

                    while True:
                        conteudo=arquivo.readline()

                        if not conteudo: # fim do arquivo
                            break
                        linha=conteudo.split(';')

                        if codigoDevolucao==linha[0]: # verifica se aquele mesmo código é encontrado em algum registro dos empréstimos
                            status=False
                            arquivo.write(f'{linha[0]};{linha[1]};{linha[2]};{linha[3]};{status}')
                            conj.remove(linha[0]) # remove código do conjunto
                            dataDevolucao=datetime.today() 
                            dataPrevista=datetime.strptime(linha[3].strip('\n'),'%d-%m-%Y') # faz a leitura de string paradate do arquivo com a data prevista da entrega
                            dif=(dataDevolucao-dataPrevista).days # calcula diferença entre a data de devolução real e a data prevista

                            if dif>0: # se a difernça é positiva quer dizer que o livro está atrasado
                                print(f'\nO livro está atrasado há {dif} dias\nUma taxa de {dif*0.5} será aplicada.')
                            else:
                                print(f'\nO livro foi devolvido dentro do prazo\nNenhuma taxa adicional será aplicada.')

                                escolherAvaliar = str(input(f'Deseja avaliar o livro: {titulo}? (s/n): ')).lower() # opção para avaliar livro

                                if escolherAvaliar.startswith('s'): # caso opte por avaliar, pede uma nota de 0 a 5 (float) e salva na lista de avaliações

                                    while True:
                                        try:

                                            avaliacao = float(input('\nInforme a nota do livro: '))
                                            if 0 <= avaliacao <= 5:
                                                print(f'\nObrigado! Avaliação registrada: {avaliacao}')

                                                dicionarioAvaliacao = {'titulo': titulo, 'avaliacao': avaliacao, 'codigo': codigo}
                                                lista.append(dicionarioAvaliacao)
                                                break
                                            else:
                                                print('\nValor inválido. Informe um valor de 0 a 5.')

                                        except ValueError:
                                            print('\nEntrada inválida. Digite apenas números!')
                                
                                else:
                                    print('\nVocê preferiu não avaliar o livro!')

                            return # evita que chegue na última menesagem abaixo
                        
    print('\nNenhum empréstimo do livro foi encontrado.') # se o código chegou aqui, quer dizer que falhou qualquer uma das verificações acima, e significa que não há empréstimo válido com o livro solicitado
        

                    

