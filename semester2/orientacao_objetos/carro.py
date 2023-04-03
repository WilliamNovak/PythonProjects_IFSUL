class carro:

    def __init__(self, cor, modelo):
        self.cor    = cor
        self.modelo = modelo

    def acelerar(self):
        print(f"Carro {self.modelo} acelerando")

    def frear(self):
        print(f"Carro {self.modelo} freando")

c1 = carro()
c2 = carro()

c1.modelo = "gol"
c2.modelo = "jetta"
c1.acelerar()

print(f'{c1.modelo}')
print(f'{c2.modelo}')