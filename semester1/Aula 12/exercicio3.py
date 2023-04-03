lista = list(map(lambda x:round(x**2,2) if x%2==0 else round(x**0.5,2), range(1,51)))
print(lista)