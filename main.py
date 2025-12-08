from menu import menuInfo
from cadastro import cadastrar, listar
from busca import buscar
from emprestimo import registrarEmprestimo
from devolucoes import devolucoesEmprestimo
from relatorio import escolherRelatorio
from registro import registrar

from datetime import datetime, timedelta
import random
import struct

FORMATO='10s50s50si20s'
TAMANHO=struct.calcsize(FORMATO)


if __name__ == "__main__":
    acervo=[]
    conjuntoEmprestados = set()

    while True:
        opt=menuInfo()

        match opt:
            case 1:
                cadastrar(acervo)

            case 2:
                listar(acervo)

            case 3:
                buscar(acervo)

            case 4:
                registrarEmprestimo(conjuntoEmprestados,acervo)

            case 5:
                devolucoesEmprestimo(conjuntoEmprestados,acervo)

            case 6:
                escolherRelatorio(conjuntoEmprestados,acervo)

            case 7:
                registrar(acervo,FORMATO)

            case 8:
                print('Encerrando programa')
                break