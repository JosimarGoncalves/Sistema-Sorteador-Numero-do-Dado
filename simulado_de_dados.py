# Simulador de dado
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem ='Vocẽ gostaria de gerar um novo valor para o o dado'

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.GerarValorDoDado()

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simular = SimuladorDeDado()
simular.Iniciar()                
