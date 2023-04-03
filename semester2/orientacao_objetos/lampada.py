class Lampada:
    ligado = False

    def __init__(self, tipo, tensao, potencia):
        self.tipo      = tipo
        self.tensao    = tensao
        self.potencia = potencia

    def ligar(self):
        print(f'A lâmpada {self.tipo} está ligando')
        self.ligado = True

    def mudar_estado(self):
        if self.ligado == True:
            self.ligado = False
        else:
            self.ligado = True

l1 = Lampada("led", 220, 15)
l2 = Lampada("halogena", 110, 20)

l1.ligar()
print(l1.ligado)
print(l2.ligado)

l1.mudar_estado()
print(l1.ligado)
l1.mudar_estado()
print(l1.ligado)