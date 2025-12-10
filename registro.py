import struct # importação da biblioteca struct responsável pela manipulação de arquivos binários
FORMATO='10s50s50si20s' # definição do formato a ser utilizado conmforme instruções do projeto
TAMANHO=struct.calcsize(FORMATO) #cálculo de tamanho em bytes através do formato anteriormente definido

def registrar(acervo): # função para registro do acervo de forma empacotada e codificada, desde que exista pelo menos um livro no acervo
    if len(acervo)==0:
        print('\nNão há livros no acervo.')
        return
    
    with open('acervo.bin','wb') as arquivo:
        for livro in acervo:
            reg=struct.pack(FORMATO,livro['codigo'].encode(),livro['titulo'].encode(),livro['autor'].encode(),livro['ano'],livro['categoria'].encode()) # .pack para empacotar as informações referentes a cada livro no acervo,
            arquivo.write(reg)                                                                                                                          # tornando-as um registro no arquivo


    print('\nAcervo salvo com sucesso.')

