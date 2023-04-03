# Criar ou sobrescrever arquivo
with open('teste.txt','w') as arq:
    arq.write('adicionando nova linha\n')
    arq.write('nova linha')

# Criar ou sobrescrever arquivo e ler
with open('teste.txt','w+') as arq:
    arq.write('adicionando nova linha\n')
    arq.write('nova linha\n')
    # Repetir linha varias vezes
    arq.write('Repete\n' * 10)
    arq.seek(0)
    print(arq.read())