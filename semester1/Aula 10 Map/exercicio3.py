lista = [[1,2],[2,3],[3,4],[4,5]]

newList = list(map(lambda x: [x[1],x[0]], lista))

print(newList)