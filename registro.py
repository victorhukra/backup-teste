import struct
FORMATO='10s50s50si20s'
TAMANHO=struct.calcsize(FORMATO)

def registrar(acervo,FORMATO):
    if len(acervo)==0:
        print('\nNão há livros no acervo')
        return
    
    with open('acervo.bin','wb') as arquivo:
        for livro in acervo:
            reg=struct.pack(FORMATO,livro['codigo'].encode(),livro['titulo'].encode(),livro['autor'].encode(),livro['ano'],livro['categoria'].encode())
            arquivo.write(reg)