import tkinter as tk
from datetime import datetime

tempo_inicial = None
botao = True

def iniciar_parar_tempo():
    global botao, tempo_inicial
    botao = not botao
    if botao:
        tempo_inicial = datetime.now()
        atualizar_tempo()

def reiniciar_tempo():
    global botao, tempo_inicial
    botao = False
    tempo_inicial = None
    label_tempo.config(text='00:00:00:00')

def atualizar_tempo():
    if botao:
        tempo = datetime.now() - tempo_inicial
        horas = tempo.seconds // 3600
        minutos = (tempo.seconds // 60) % 60
        segundos = tempo.seconds % 60
        milissegundos = tempo.microseconds // 10000
        tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}:{milissegundos:02}"
        label_tempo.config(text=tempo_formatado)
        label_tempo.after(10, atualizar_tempo)

janela = tk.Tk()
janela.geometry('1366x768')
janela.title('Contador')

label_tempo = tk.Label(janela, text='00:00:00:00', font=('arial', 180))
label_tempo.place(relx=0.5, rely=0.3, anchor='center')

botao_parar = tk.Button(janela, text='Iniciar/Parar', font=('arial', 60), command=iniciar_parar_tempo, bg='gray')
botao_parar.place(relx=0.5, rely=0.6, anchor='center')

botao_reiniciar = tk.Button(janela, text='Reiniciar', font=('arial', 40), command=reiniciar_tempo, bg='red')
botao_reiniciar.place(relx=0.5, rely=0.8, anchor='center')

janela.mainloop()
