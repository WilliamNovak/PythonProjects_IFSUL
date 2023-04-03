s = input('Diga uma string: ')

# A
m = s.upper()
print(m)

# B
n = s.lower()
print(n)

# C
c = s.split(' ')
r = ''
for x in range(0,len(c)):
    r = r + ' ' + c[x].capitalize()

print(r.lstrip())