from datetime import datetime, timedelta

def registrarEmprestimo(conj, acervo):
    if len(acervo)==0:
        print('\nNão há livros no acervo.')
        return

    data = datetime.today()

    diasDevolucao = timedelta(days=7)
    dataDevolucao = data + diasDevolucao

    dataEmprestimo = data.strftime('%d-%m-%Y')
    dataPrevistaDevolucao = dataDevolucao.strftime('%d-%m-%Y')

    nomeUsuario = input('\nNome - Usuário: ')
    emprestarLivro = input(f'Olá {nomeUsuario}! Informe o título do livro que deseja emprestar: ')

    encontrado = False  #variável que será utilizada para verificar se o livro que deseja emprestar existe de fato no acervo
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

    emprestimo = (codigoEncontrado, nomeUsuario, dataEmprestimo, dataPrevistaDevolucao)
    conj.add(codigoEncontrado)

    with open('usuarios.txt', 'a') as file:
        file.write(f'{nomeUsuario}\n')

    with open('emprestimos.txt', 'a') as file:
        file.write(f'{emprestimo[0]};{emprestimo[1]};{emprestimo[2]};{emprestimo[3]}\n')


    print('\nEmpréstimo registrado com sucesso.')

