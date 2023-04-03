# Cria funcao com return
def funcao():
    return(5+10)

# Recebe e imprime o resultado
x = funcao()
print(x)

# Funcao com multiplos retornos
def funcao2():
    return 5, 10

x, y = funcao2()
print(f'X: {x}, Y: {y}')

# Funcao com parametros com valor default
def subtracao(a = 5, b = 25):
    return b - a

x = subtracao(10)
print(x)

# FUNCAO DENTRO DE OUTRA
# Cria funcao soma
def soma(a,b):
    return a+b

# Cria funcao mat com parametro f como padrao Soma
def mat(a,b,f=soma):
    return f(a,b)

# Printa o resultado de mat, passando parametros para A e B que serao passados para funcao soma que é chamada usando F
print(mat(5,7))

# USAR VARIAVEL GLOBAL DENTRO DE FUNCAO
n = 0

def incrementa():
    global n
    n = n + 1
    return n

print(incrementa())
print(incrementa())
print(incrementa())

# Passar parametros extras *args
def teste(a, b, *args):
    print(a)
    print(b)
    print(args)

teste(1,2,5,7,3,5)

# Somar todos parametros passados
def somaTodos(*args):
    return sum(args)

print(somaTodos(1,2,5,5,6,3,5,7,7,3,5))

# Passar lista como parametro para o *args
# Desempacotamento *lista
l = [1,2,3,4,5]
print(somaTodos(*l))