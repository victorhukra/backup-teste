from datetime import datetime, timedelta

def devolucoesEmprestimo(conj,acervo): #aqui temos um problema com as datas, como cada empréstimo tem um limites de 7 dias, testando o código nunca vai dar uma devolução atrasada
    if len(acervo)==0:
        print('\nNão há livros no acervo')
        return
    
    devolucao=str(input('\nDigite o nome do livro a ser devolvido: '))
    for registro in acervo: 

        if registro['titulo']==devolucao: 
            codigoDevolucao=registro['codigo']

            if codigoDevolucao in conj:
                with open('emprestimos.txt','r') as arquivo:

                    while True:
                        conteudo=arquivo.readline()

                        if not conteudo:
                            break
                        linha=conteudo.split(';')

                        if codigoDevolucao==linha[0]:
                            conj.remove(linha[0])
                            dataDevolucao=datetime.today() #talvez seja necessário alterar isso por input (no Empréstimo também)
                            dataPrevista=datetime.strptime(linha[3].strip('\n'),'%d-%m-%Y')
                            dif=(dataDevolucao-dataPrevista).days

                            if dif>0:
                                print(f'\nO livro está atrasado há {dif} dias\nUma taxa de {dif*0.5} será aplicada')
                            else:
                                print(f'\nO livro foi devolvido dentro do prazo\nNenhuma taxa adicional será aplicada')

                            return
                        
                    print('\nNenhum empréstimo do livro foi encontrado')
        
                    