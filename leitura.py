import struct
FORMATO='10s50s50si20s'
TAMANHO=struct.calcsize(FORMATO)

def importar():
    acervo=[]
    try:
        with open('acervo.bin','rb') as arquivo: # faz a leitura de cada linha até chegar numa linha vazia (fim do arquivo), desempacotando os valores de cada livro presente no acervo.bin
            while True:
                linha=arquivo.read(TAMANHO)
                if not linha:
                    break
                b_codigo,b_titulo,b_autor,ano,b_categoria=struct.unpack(FORMATO,linha)
                dadosLivros = {'codigo': b_codigo.strip(b'\x00').decode(), 'titulo': b_titulo.strip(b'\x00').decode(), 'autor': b_autor.strip(b'\x00').decode(), 'ano': ano, 'categoria': b_categoria.strip(b'\x00').decode()} #gera dicionário com os valores recebidos
                acervo.append(dadosLivros) #salva no acervo
            return acervo
    except FileNotFoundError:
        print('Acervo não encontrado')

def emprestados():
    emprestados=set()
    try:
        with open('emprestimos.txt','r') as arquivo: # faz a leitura dos empréstimos e se o status for ativo, salva no conjunto de livros já emprestados
            while True:
                linha=arquivo.readline()
                if not linha:
                    break
                conteudo=linha.split(';')
                if conteudo[4].strip()=='Ativo':
                    emprestados.add(conteudo[0])
            return emprestados
    except FileNotFoundError:
        print('Registro de empréstimos não encontrado')
