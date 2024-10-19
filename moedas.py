import tkinter as tk
from tkinter import *
import requests


def atualizar_valores():
    link = "https://api.exchangerate-api.com/v4/latest/BRL"
    
    try:
        req = requests.get(link)
        req.raise_for_status()
        
        data = req.json()

        usd_brl = data['rates']['USD']
        eur_brl = data['rates']['EUR']
        
        brl_for_usd = 1 / usd_brl
        brl_for_eur = 1 / eur_brl
        
        return brl_for_usd, brl_for_eur
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None, None

brl_for_usd, brl_for_eur = atualizar_valores()


janela = tk.Tk()
janela.geometry('600x400')
janela.title('moedas')
janela.config(bg='#1C1C1C')


label_euro = tk.Label(text='EURO', font=('arial',26))
label_euro.place(x=190,y=140, width=200)

label_dolar = tk.Label(text='DOLAR', font=('arial',26))
label_dolar.place(x=190,y=270, width=200)


label_euro1 = tk.Label(text=f"{brl_for_eur:.2f}", font=('arial',26), bg=('#1C1C1C'), fg='white')
label_euro1.place(x=190,y=200, width=200)


label_dolar1 = tk.Label(text=f"{brl_for_usd:.2f}", font=('arial',26 ))
label_dolar1.place(x=190,y=330, width=200)

janela.mainloop()