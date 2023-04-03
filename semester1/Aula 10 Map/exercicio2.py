lista = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x:[x, x*x], lista))

print(newList)