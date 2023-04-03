dic = {}
s = 'sapiranga'

for letra in s:
    if letra not in dic:
        dic[letra]=1
    else:
        dic[letra]=dic[letra]+1

print(dic)
