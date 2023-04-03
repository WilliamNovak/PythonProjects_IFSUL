# Importa meu modulo criado
import meu_modulo

# Utilizacao funcao de meu modulo
print(meu_modulo.soma(2,5))

# Importa funcao especifica do meu modulo
from meu_modulo import subtracao

# Utiliza funcao importada
print(subtracao(7,2))

# Importa todas funcoes do meu modulo
from meu_modulo import *
print(multi(5,2))
print(divisao(10,2))