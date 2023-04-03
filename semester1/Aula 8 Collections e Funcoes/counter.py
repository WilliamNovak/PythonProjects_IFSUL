# Importa método Counter
from collections import Counter

# Cria string
s = "isogsiogbruiohhjibmfbklea"

# Conta frequencia de cada caracter na string
r = Counter(s)

# Printa frequencia
print(r)

# Printa os dois caracteres com mais frequencia
print(r.most_common(2))