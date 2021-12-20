# Simulador de dado
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem ='Vocẽ gostaria de gerar um novo valor para o o dado'
        
        
        



    def Iniciar(self):
        
        #Layout
        layout =[
            [sg.Text('Jogar o dado')],
            [sg.Button('sim')],[sg.Button('nao')]
        ]
        
        #Criar uma Janela
        self.janela = sg.Window('Simulador de Dado',Layout=layout)
        
        #Ler os Arquivos da Tela
        self.eventos, self.valores = self.janela.Read()
        
        #Fazer alguma coisa com esses valores 
        while True:
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
