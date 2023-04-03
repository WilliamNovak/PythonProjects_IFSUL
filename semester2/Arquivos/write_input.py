# adicionar conteúdo no arquivo até digitar sair
with open('teste.txt','w+') as arq:
    while True:
        x = input('Digite uma palavra ou sair:')
        if(x != 'sair'):
            arq.write(x + '\n')
        else:
            break
    arq.seek(0)
    print(arq.read())