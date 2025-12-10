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
