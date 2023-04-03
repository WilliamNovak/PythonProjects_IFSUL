class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def formatData(self):
        return "{}/{}/{}".format("{:02d}".format(self.__dia), "{:02d}".format(self.__mes), self.__ano)

try:
    ano = int(input('Informe o ano: '))
    try:
        mes = int(input('Informe o mês: '))
        
        if(mes < 1 or mes > 12):
            print('Mês inválido!')
        else:
            try:
                dia = int(input('Informe o dia: '))
                if dia < 1:
                    print('Dia inválido!')
                elif (mes in (1, 3, 5, 7, 8, 10, 12) and dia > 31):
                    print('Dia inválido! O mês tem 31 dias.')
                elif (mes in (4,6,9,11) and dia > 30):
                    print('Dia inválido! O mês tem 30 dias.')
                elif (mes == 2):
                    print('Dia inválido! O mês tem 28 dias.')
                else:
                    data = Data(dia,mes,ano)
                    print(f'Data formatada: {data.formatData()}')
            except:
                print('Dia inválido!')
    except:
        print('Mês inválido!')
except:
    print('Ano inválido!')