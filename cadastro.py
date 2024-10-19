import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def adicionar_dados():
    nome = entry_nome.get()
    senha = entry_senha.get()
    email = entry_email.get()
    tudo = nome, senha, email
    achar = email.find('@gmail.com')


    if not nome and not senha and not email:
        messagebox.showerror(title='erro',message='por favor, preencha todas as caixas')

    elif achar == -1:
        messagebox.showerror(title='erro', message='por favor, insira um email valido')


    elif nome and senha and email:
        tree.insert("", 'end', values=tudo)

        entry_nome.delete(0,tk.END)
        entry_senha.delete(0,tk.END)
        entry_email.delete(0,tk.END)

def excluir_dados():
    selecionado = tree.selection()
    if selecionado:
        for item in selecionado:
            values = tree.item(item, 'values')
            tree.delete(item)


            
    else:
        messagebox.showerror(title='erro',message='por favor, selecione algo para excluir')

janela = tk.Tk()
janela.geometry('700x400')
janela.title('cadastro e login')

style = ttk.Style()
style.configure("Treeview", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

notebook = ttk.Notebook(janela)
notebook.place(x=-1, y=-1, width=800, height=500)

login = tk.Frame(notebook, bg='#1C1C1C')
cadastro = tk.Frame(notebook, bg='#1C1C1C')

notebook.add(cadastro, text='cadastro')

# CADASTRO
    # nomes
label_nome = tk.Label(cadastro, text='nome', font=("arial", 17))
label_nome.place(x=5, y=10, width=90)
entry_nome = tk.Entry(cadastro, font=("arial", 19))
entry_nome.place(x=90, y=10, width=600)

label_senha = tk.Label(cadastro, text='senha', font=("arial", 17))
label_senha.place(x=5, y=50, width=90)
entry_senha = tk.Entry(cadastro, font=("arial", 19))
entry_senha.place(x=90, y=50, width=600)

label_email = tk.Label(cadastro, text='email', font=("arial", 17))
label_email.place(x=5, y=90, width=90)
entry_email = tk.Entry(cadastro, font=("arial", 19))
entry_email.place(x=90, y=90, width=600)

label_cadastrar = tk.Label(cadastro, text='cadastro de clientes', font=("arial", 28))
label_cadastrar.place(x=220, y=130, width=450)

    # botoes
botao_criar = tk.Button(cadastro, text='CRIAR', bg='green', font=("arial", 15), command=adicionar_dados)
botao_criar.place(x=5, y=130)

botao_deletar = tk.Button(cadastro, text='EXCLUIR', bg='red', font=("arial", 15), command=excluir_dados)
botao_deletar.place(x=90, y=130)

    # treeview

tree = ttk.Treeview(cadastro, columns=('nome', 'senha', 'email'), show='headings')

tree.heading('nome', text='nome')
tree.heading('senha', text='senha')
tree.heading('email', text='email')

tree.column('nome', anchor='center', width=250)
tree.column('senha', anchor='center', width=250)
tree.column('email', anchor='center', width=250)


tree.place(x=-1, y=180)


janela.mainloop()