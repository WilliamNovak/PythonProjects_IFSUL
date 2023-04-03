class Televisao:
    status = False
    mutada = False

    def __init__(self, canal, volume, tamanho, marcamodelo, canalMin, canalMax):
        self.canal       = canal
        self.volume      = volume
        self.tamanho     = tamanho
        self.marcamodelo = marcamodelo
        self.canalMin    = canalMin
        self.canalMax    = canalMax

    def mudarCanal(self, canal):
        if self.status == True:
            try:
                canal = int(canal)
                if canal >= self.canalMin and canal <= self.canalMax:
                    self.canal = canal
                    print(f"Trocado para o canal {canal}.")
                else:
                    print("Canal inexistente.")
            except:
                print(f"Erro: Digite apenas canais numéricos entre {self.canalMin} e {self.canalMax}.")
        else:
            print("Televisão desligada!")
    
    def mudarVolume(self,volume):
        if self.status == True:
            try:
                volume = int(volume)
                if volume >= 0 and volume <= 100:
                    self.volume = volume
                    print(f"Volume alterado para {volume}.")
                    self.mutada = False
                else:
                    print("Volume inexistente.")
            except:
                print("Erro: Digite apenas volumes numéricos entre 0 e 100.")
        else:
            print("Televisão desligada!")

    def aumentarVolume(self):
        if self.volume == 100:
            self.volume = 0
        else:
            self.volume += 1
        self.mutada = False
        print(f'Volume aumentado para {self.volume}.')

    def diminuirVolume(self):
        if self.volume == 0 :
            self.volume = 100
        else:
            self.volume -= 1
        self.mutada = False
        print(f'Volume diminuído para {self.volume}.')

    def mutar(self):
        if self.mutada == False:
            self.mutada = True
            print('Televisão no mutada.')
        else:
            self.mutada = False
            print('Televisão desmutada.')

    def ligar(self):
        if self.status == False:
            self.status = True
            print(f"Televisão ligada com sucesso.")
        else:
            print(f"Televisão já está ligada.")

    def desligar(self):
        if self.status == True:
            self.status = False
            print(f"Televisão desligada com sucesso.")
        else:
            print("Televisão já está desligada.")

    def mostraStatus(self):
        print(f'-- Televisão --')
        print(f'Marca: {self.marcamodelo}')
        print(f'Tamanho: {self.tamanho} polegadas')
        print(f'Canais: {self.canalMin} a {self.canalMax}')
        print(f'Canal: {self.canal}')
        print(f'Volume: {self.volume}')
        print(f'Som: {"mutado" if self.mutada == True else "desmutado"}')
        print(f'A televisão está {"ligada" if self.status == True else "desligada"}')

t1 = Televisao(15,12,50,"LG", 2, 50)
t2 = Televisao(23,7,35,"Sony", 10, 78)

opcao = 1

while opcao != 0:
    print(f'Menu:\n1 - Televisão 1\n2 - Televisão 2\n0 - Sair')
    try:
        opcao = int(input('Selecione o dispositivo para visualizar ou sair: '))

        if opcao < 0 or opcao > 2:
            print('Opção inválida!')
        elif opcao != 0:
            if opcao == 1:
                tv = t1
            else:
                tv = t2

            print(f'Opções:\n1 - Ligar\n2 - Desligar\n3 - Mudal canal\n4 - Mudar volume\n5 - Aumentar volume\n6 - Diminuir volume\n7 - Mutar/Desmutar\n8 - Status\n9 - Voltar')
            
            try:
                opcao2 = int(input('Qual opção deseja realizar? '))

                if opcao2 == 1:
                    tv.ligar()
                elif opcao2 == 2:
                    tv.desligar()
                elif opcao2 == 3:
                    canal = input("Informe o canal que deseja assistir: ")
                    tv.mudarCanal(canal)
                elif opcao2 == 4:
                    volume = input("Informe o volume que deseja escutar (0 a 100): ")
                    tv.mudarVolume(volume)
                elif opcao2 == 5:
                    tv.aumentarVolume()
                elif opcao2 == 6:
                    tv.diminuirVolume()
                elif opcao2 == 7:
                    tv.mutar()
                elif opcao2 == 8:
                    tv.mostraStatus()
                elif opcao2 == 9:
                    print(f'*'*12)
                else:
                    print('Opção inválida!')

            except:
                print('Opção inválida!')

        else:
            print('Menu finalizado.')
    except:
        print('Erro: Opção inválida!')