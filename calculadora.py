import tkinter as tk
from tkinter import *

# Funções de operação
def adicionar_numero(text):
    current_text = visor.cget('text')
    visor.config(text=current_text + text)

def definir_operacao(op):
    global operador
    global numero_anterior
    numero_anterior = visor.cget('text')
    operador = op
    visor.config(text='')

def calcular():
    global numero_anterior
    global operador

    numero_atual = visor.cget('text')
    
    if numero_anterior and numero_atual and operador:
        try:
            resultado = eval(f"{numero_anterior} {operador} {numero_atual}")
            visor.config(text=str(resultado))
        except Exception as e:
            visor.config(text="Erro")
        finally:
            numero_anterior = ''
            operador = ''

def apagar():
    visor.config(text='')

# Configurações da janela
janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('305x385')
janela.config(bg='#1C1C1C')

# Visor
visor = tk.Label(text='', font=("arial", 35), anchor='e')
visor.place(x=3, y=10, width=300)

# Botões numéricos
botao_0 = tk.Button(text=' 0 ', font=("arial", 26), command=lambda: adicionar_numero('0'))
botao_0.place(x=5, y=311, width=68)

botao_1 = tk.Button(text=' 1 ', font=("arial", 26), command=lambda: adicionar_numero('1'))
botao_1.place(x=5, y=234)

botao_2 = tk.Button(text=' 2 ', font=("arial", 26), command=lambda: adicionar_numero('2'))
botao_2.place(x=80, y=234)

botao_3 = tk.Button(text=' 3 ', font=("arial", 26), command=lambda: adicionar_numero('3'))
botao_3.place(x=155, y=234)

botao_4 = tk.Button(text=' 4 ', font=("arial", 26), command=lambda: adicionar_numero('4'))
botao_4.place(x=5, y=157)

botao_5 = tk.Button(text=' 5 ', font=("arial", 26), command=lambda: adicionar_numero('5'))
botao_5.place(x=80, y=157)

botao_6 = tk.Button(text=' 6 ', font=("arial", 26), command=lambda: adicionar_numero('6'))
botao_6.place(x=155, y=157)

botao_7 = tk.Button(text=' 7 ', font=("arial", 26), command=lambda: adicionar_numero('7'))
botao_7.place(x=5, y=80)

botao_8 = tk.Button(text=' 8 ', font=("arial", 26), command=lambda: adicionar_numero('8'))
botao_8.place(x=80, y=80)

botao_9 = tk.Button(text=' 9 ', font=("arial", 26), command=lambda: adicionar_numero('9'))
botao_9.place(x=155, y=80)

# Botões de operação
botao_del = tk.Button(text=' C ', font=("arial", 26), command=apagar)
botao_del.place(x=230, y=80, width=68)

botao_igual = tk.Button(text=' = ', font=("arial", 26), command=calcular)
botao_igual.place(x=230, y=157, width=68)

botao_soma = tk.Button(text=' + ', font=("arial", 26), command=lambda: definir_operacao('+'))
botao_soma.place(x=230, y=234, width=68)

botao_menos = tk.Button(text=' - ', font=("arial", 26), command=lambda: definir_operacao('-'))
botao_menos.place(x=230, y=311, width=68)

botao_vezes = tk.Button(text=' X ', font=("arial", 26), command=lambda: definir_operacao('*'))
botao_vezes.place(x=155, y=311, width=68)

botao_dividir = tk.Button(text=' ÷ ', font=("arial", 26), command=lambda: definir_operacao('/'))
botao_dividir.place(x=80, y=311, width=68)

# Inicializa variáveis
numero_anterior = ''
operador = ''

janela.mainloop()
