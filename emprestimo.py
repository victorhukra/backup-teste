from datetime import datetime, timedelta # importação da biblioteca datetime para manipulação de datas

def registrarEmprestimo(conj, acervo): # função responsável pelo registro do empréstimo no acervo, caso a quantidade de livros seja maior que 1
    if len(acervo)==0:
        print('\nNão há livros no acervo.')
        return

    data = datetime.today() # inicializando a data como a data de hoje

    diasDevolucao = timedelta(days=7) # o número de dias para a devolução sem taxa sendo 7
    dataDevolucao = data + diasDevolucao

    dataEmprestimo = data.strftime('%d-%m-%Y')                 # formatação de ambas as datas, seguindo
    dataPrevistaDevolucao = dataDevolucao.strftime('%d-%m-%Y') # a estrutura 10/10/2010 por exemplo

    nomeUsuario = input('\nNome - Usuário: ')
    emprestarLivro = input(f'Olá {nomeUsuario}! Informe o título do livro que deseja emprestar: ')

    encontrado = False  # variável que será utilizada para verificar se o livro que deseja emprestar existe de fato no acervo
    codigoEncontrado = None

    for elemento in acervo:
        if emprestarLivro.lower() in elemento['titulo'].lower():
            encontrado = True
            codigoEncontrado = elemento['codigo']
            break  

    if not encontrado:
        print('Livro não encontrado no acervo.')
        return  

    if codigoEncontrado in conj:
        print('Este livro já foi emprestado.')
        return

    status=True
    emprestimo = (codigoEncontrado, nomeUsuario, dataEmprestimo, dataPrevistaDevolucao, status) # definição do empréstimo passando informações que serão utilizadas na manipulação de arquivos .txt
    conj.add(codigoEncontrado)

    
    repetido=False
    try:
        with open('usuarios.txt','r') as file:
            for linha in file:
                if linha.strip(' \n')==nomeUsuario:
                    repetido=True
                    break
    except FileNotFoundError:
        pass
    
    if not repetido: # se o usuário não está no arquivo usuarios.txt, seu nome é adicionado
        with open('usuarios.txt','a') as file:
            file.write(f'{nomeUsuario}\n')

    with open('emprestimos.txt', 'a') as file:
        file.write(f'{emprestimo[0]};{emprestimo[1]};{emprestimo[2]};{emprestimo[3]};{emprestimo[4]}\n')


    print('\nEmpréstimo registrado com sucesso.')

