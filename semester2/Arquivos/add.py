# Acrescentar conteúdo arquivo, sem apagar oq já existe
with open('teste.txt','a+') as arq:
    arq.write('adicionando nova linha\n')
    arq.write('sem apagar')
    arq.seek(0)
    print(arq.read())