from datetime import datetime
from tkinter import *
import tkinter as tk
 
def atualizar():
    hoje = datetime.now() 
    data_formatada = hoje.strftime('%d/%m/%Y')
    tempo_formatado = hoje.strftime('%H:%M:%S')
    
    label_tempo.config(text=f'{tempo_formatado}')
    label_data.config(text=f'{data_formatada}')
    janela.after(1000, atualizar)

janela = tk.Tk()
janela.geometry('1366x768')
janela.title('relogio')

label_tempo = tk.Label(font=("arial",180))
label_tempo.place(x=200,y=250)

label_data = tk.Label(font=("arial",90))
label_data.place(x=350,y=100)

atualizar()
janela.mainloop()



