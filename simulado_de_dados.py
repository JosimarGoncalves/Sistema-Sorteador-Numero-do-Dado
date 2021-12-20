# Simulador de dado
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem ='Vocẽ gostaria de gerar um novo valor para o o dado'
        #Layout
        self.layout =[
            [sg.Text('Jogar o dado')],
            [sg.Button('sim')],[sg.Button('nao')]
        ]

    def Iniciar(self):   
        
        #Criar uma Janela
        ##window = sg.Window('Simulador de Dado', layout)
        self.janela = sg.Window('Window Title',layout=self.layout)
        
        #Ler os Arquivos da Tela
        self.eventos, self.valores = self.janela.Read()
        
        #Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos =='s':
                self.GerarValorDoDado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou nao')
        except:
            print('Ocorreu um erro ao receber sua resposta!') 
        
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simular = SimuladorDeDado()
simular.Iniciar()                
