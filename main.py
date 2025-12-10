# importações necessárias para o funcionamento do programa
from menu import menuInfo
from cadastro import cadastrar, listar
from busca import buscar
from emprestimo import registrarEmprestimo
from devolucoes import devolucoesEmprestimo
from relatorio import escolherRelatorio
from registro import registrar
from leitura import importar, emprestados

if __name__ == "__main__": # permite a inicialização do projeto
    acervo=importar()
    conjuntoEmprestados = emprestados()
    listaAvaliacao = []
    atualizado=True

    while True: # loop para escolha de opções disponíveis no menu, até que o usuário digite 8 para encerrar o loop e sair do programa
        opt=menuInfo()

        match opt:
            case 1:
                cadastrar(acervo)
                atualizado=False

            case 2:
                listar(acervo)

            case 3:
                buscar(acervo)

            case 4:
                registrarEmprestimo(conjuntoEmprestados,acervo)

            case 5:
                devolucoesEmprestimo(conjuntoEmprestados,acervo,listaAvaliacao)

            case 6:
                escolherRelatorio(conjuntoEmprestados,acervo,listaAvaliacao)

            case 7:
                registrar(acervo)
                atualizado=True

            case 8:
                if not atualizado:
                    print('\nAviso! O acervo está desatualizado, antes de sair lembre-se de salvar as alterações')
                else:
                    print('\nEncerrando programa.')
                    break
