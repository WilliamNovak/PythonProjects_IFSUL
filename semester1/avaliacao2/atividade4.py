fun1 = [28940, 28942, 28966, 28944, 28985, 28947, 28948, 28950, 28951, 28952, 28953, 28954, 28946, 28960, 28962, 28963, 28967, 28975, 28982, 28996]
c1 = set(fun1)
fun2 = [28964, 28990, 28992, 28994, 28995, 28986, 28985, 28978, 28979, 28991, 28990, 28983, 28984, 28955, 28956, 28958, 28961, 28946, 28994, 28949]
c2 = set(fun2)
fun3 = [28997, 28965, 28966, 28999, 28989, 28987, 28988, 28970, 28993, 28998, 28968, 28969, 28973, 28974, 28972, 28977, 28981, 28980, 28976, 28941, 28993]
c3 = set(fun3)

a = c1&c2

if(len(a) > 0):
    print(f'Há {len(a)} itens repetidos entre Funcionário 1 e Funcionário 2, são eles: {a}')
else:
    print('Não há itens repetidos entre Funcionário 1 e Funcionário 2')

b = c1&c3

if(len(b) > 0):
    print(f'Há {len(b)} itens repetidos entre Funcionário 1 e Funcionário 3, são eles: {b}')
else:
    print('Não há itens repetidos entre Funcionário 1 e Funcionário 3')

c = c2&c3

if(len(c) > 0):
    print(f'Há {len(c)} itens repetidos entre Funcionário 2 e Funcionário 3, são eles: {c}')
else:
    print('Não há itens repetidos entre Funcionário 2 e Funcionário 3')

d = c1&c2&c3

if(len(d) > 0):
    print(f'Há {len(d)} itens repetidos entre Funcionário 1, Funcionário 2 e Funcionário 3, são eles: {d}')
else:
    print('Não há itens repetidos entre Funcionário 1, Funcionário 2 e Funcionário 3')