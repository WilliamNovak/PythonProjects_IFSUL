fun1 = [28940, 28942, 28966, 28944, 28985, 28947, 28948, 28950, 28951, 28952, 28953, 28954, 28946, 28960, 28962, 28963, 28967, 28975, 28982, 28996]

c1 = set(fun1)
rep1 = len(fun1) - len(c1)

if (rep1 > 0):
    print(f'Funcionário 1 repetiu {rep1} de seus itens.')

fun2 = [28964, 28990, 28992, 28994, 28995, 28986, 28985, 28978, 28979, 28991, 28990, 28983, 28984, 28955, 28956, 28958, 28961, 28946, 28994, 28949]

c2 = set(fun2)
rep2 = len(fun2) - len(c2)

if (rep2 > 0):
    print(f'Funcionário 2 repetiu {rep2} de seus itens.')

fun3 = [28997, 28965, 28966, 28999, 28989, 28987, 28988, 28970, 28993, 28998, 28968, 28969, 28973, 28974, 28972, 28977, 28981, 28980, 28976, 28941, 28993]

c3 = set(fun3)
rep3 = len(fun3) - len(c3)

if (rep3 > 0):
    print(f'Funcionário 3 repetiu {rep3} de seus itens.')