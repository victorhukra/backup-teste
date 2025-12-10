def menuInfo(): # função que define o menu com as opções para escolha do usuário
    print("\nMenu de opções")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livros")
    print("4 - Registrar empréstimo")
    print("5 - Registrar devolução")
    print("6 - Gerar relatórios")
    print("7 - Salvar acervo")
    print("8 - Sair\n")

    while True: # loop para verificação de valores até que o usuário escolha uma opção válida
        try:
            opcao = int(input("Digite a opção desejada: "))

            if opcao<1 or opcao>8:
                raise IndexError
            
            return opcao
        
        except ValueError:
            print('Digite um número inteiro correspondente.')
            
        except IndexError:
            print('Entrada inválida, digite um número de 1 a 8.')



