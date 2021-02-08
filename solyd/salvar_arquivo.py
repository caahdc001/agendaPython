try:
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('Pietra\n')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)



    # 'r' - abre para ler;
    # 'w' - abre para escrever / arquivo é soberscrito
    # 'a' - abre para escrever / novo conteúdo é adicionado ao final do arquivo
    # 'b' - modo de arquivo binário