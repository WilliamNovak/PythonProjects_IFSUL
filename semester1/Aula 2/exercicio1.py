s = "MANIPULAÇÃO DE STRING"

# A
print(s[:])

# B
print(s[0])

# C
print(s[len(s)-1])

# D
print(s[0:11])

# E
print(s[12:14])

# F
print(s[15:len(s)])

# G
for x in range(0,len(s)):
    if x % 2 != 0:
        print(s[x])

# H
for x in range(0,len(s)):
    if x % 2 == 0:
        print(s[x])

# I
z = ''
for x in range(len(s)-1,-1,-1):
    z = z + s[x]

print(z)