from hashlib import new


lista = [1,4,7,2,34,17,4,8,34,3,5]

newList = list(map(lambda x: (x,'par') if x%2==0 else (x,'ímpar'),lista))

print(newList)