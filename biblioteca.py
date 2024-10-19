import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta

hoje = datetime.now()
datas = hoje.strftime("%d/%m/%y")

janela = tk.Tk()
janela.title('sistema da biblioteca')
janela.geometry('700x400')

style = ttk.Style()
style.configure("Treeview", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# CRIAÇÃO DE ABAS
notebook = ttk.Notebook(janela)
notebook.place(x=-1, y=-1, width=800, height=500)

alunos = tk.Frame(notebook, bg='#1C1C1C')
livros = tk.Frame(notebook, bg='#1C1C1C')

notebook.add(alunos, text='alunos')
notebook.add(livros, text='livros')

# Dados fictícios
alunos_data = []
livros_data = []

# FUNÇÕES DE PESQUISA
def pesquisar_alunos():
    busca = entry_pesquisar.get().strip().lower()
    for item in tree1.get_children():
        tree1.delete(item)
    
    for aluno in alunos_data:
        if busca in aluno[0].lower():
            tree1.insert("", 'end', values=aluno)

def pesquisar_livros():
    busca = entry_pesquisar_livros.get().strip().lower()
    for item in tree2.get_children():
        tree2.delete(item)
    
    for livro in livros_data:
        if busca in livro[0].lower() or busca in livro[1].lower() or busca in livro[2].lower():
            tree2.insert("", 'end', values=livro)
    atualizar_cor_livros()

# FUNÇÕES
def verificar_codigo_livro(codigo):
    for item in tree2.get_children():
        livro_codigo = tree2.item(item, 'values')[2]
        if livro_codigo == codigo:
            return tree2.item(item, 'values')[0]  # Nome do livro
    return None

def verificar_livro_emprestado(codigo):
    for item in tree1.get_children():
        if tree1.item(item, 'values')[2] == codigo:
            return True
    return False

def adicionar_dados1():
    nome = entry_nome.get()
    turma = entry_turma.get()
    codigo1 = entry_codigo1.get()
    livro_retirado = verificar_codigo_livro(codigo1)
    
    if nome and turma and codigo1:
        if livro_retirado:
            if verificar_livro_emprestado(codigo1):
                messagebox.showwarning("Livro já emprestado", "O livro com esse código já foi emprestado.")
            else:
                data_atual = datetime.now()
                data_futura = data_atual + timedelta(days=15)
                datas = data_atual.strftime("%d/%m/%y")
                data_devolucao = data_futura.strftime("%d/%m/%y")
                
                aluno = (nome, turma, codigo1, livro_retirado, f"{datas} - {data_devolucao}")
                alunos_data.append(aluno)
                tree1.insert("", 'end', values=aluno)
                atualizar_cor_livros()
                entry_nome.delete(0, tk.END)
                entry_turma.delete(0, tk.END)
                entry_codigo1.delete(0, tk.END)
        else:
            messagebox.showwarning("Código inválido", "O código do livro não está cadastrado.")
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

def excluir_dados1():
    selecionado = tree1.selection()
    if selecionado:
        for item in selecionado:
            values = tree1.item(item, 'values')
            alunos_data.remove(tuple(values))
            tree1.delete(item)
        atualizar_cor_livros()
    else:
        messagebox.showwarning("Nenhum item selecionado", "Por favor, selecione um item para deletar.")

def adicionar_dados2():
    livro = entry_livro.get()
    genero = entry_genero.get()
    codigo2 = entry_codigo2.get()

    if livro and genero and codigo2:
        if any(livro[2] == codigo2 for livro in livros_data):
            messagebox.showwarning("Código duplicado", "Já existe um livro com esse código.")
        else:
            livro_data = (livro, genero, codigo2)
            livros_data.append(livro_data)
            tree2.insert("", 'end', values=livro_data)
            entry_livro.delete(0, tk.END)
            entry_genero.delete(0, tk.END)
            entry_codigo2.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

def excluir_dados2():
    selecionado = tree2.selection()
    if selecionado:
        for item in selecionado:
            values = tree2.item(item, 'values')
            codigo_livro = values[2]
            if verificar_livro_emprestado(codigo_livro):
                messagebox.showwarning("Livro emprestado", "Não é possível excluir um livro que está emprestado.")
            else:
                livros_data.remove(tuple(values))
                tree2.delete(item)
        atualizar_cor_livros()
    else:
        messagebox.showwarning("Nenhum item selecionado", "Por favor, selecione um item para deletar.")

def atualizar_cor_livros():
    emprestados = {item[2] for item in alunos_data}
    for item in tree2.get_children():
        livro_codigo = tree2.item(item, 'values')[2]
        if livro_codigo in emprestados:
            tree2.item(item, tags=('emprestado',))
        else:
            tree2.item(item, tags=('disponivel',))
    tree2.tag_configure('emprestado', background='red')
    tree2.tag_configure('disponivel', background='#ffffff')

def renovar_livro():
    selecionado = tree1.selection()
    if selecionado:
        for item in selecionado:
            values = tree1.item(item, 'values')
            data_atual = datetime.now()
            data_devolucao = values[4].split(' - ')[1]
            data_devolucao = datetime.strptime(data_devolucao, "%d/%m/%y")
            nova_data_devolucao = data_devolucao + timedelta(days=15)
            nova_data_devolucao_str = nova_data_devolucao.strftime("%d/%m/%y")
            novo_valor = f"{values[4].split(' - ')[0]} - {nova_data_devolucao_str}"
            tree1.item(item, values=(values[0], values[1], values[2], values[3], novo_valor))
            for i, aluno in enumerate(alunos_data):
                if aluno[2] == values[2]:
                    alunos_data[i] = (aluno[0], aluno[1], aluno[2], aluno[3], novo_valor) 
            messagebox.showinfo("Renovação", "Data de devolução renovada com sucesso.")
    else:
        messagebox.showwarning("Nenhum item selecionado", "Por favor, selecione um item para renovar.")

# TREEVIEW DE ALUNOS
tree1 = ttk.Treeview(alunos, columns=('nome', 'turma', 'codigo1', 'livro', 'datas'), show='headings')
tree1.heading('nome', text='nome')
tree1.heading('turma', text='turma')
tree1.heading('codigo1', text='codigo')
tree1.heading('livro', text='livro')
tree1.heading('datas', text='datas')

tree1.column('nome', anchor='center', width=200)
tree1.column('turma', anchor='center', width=60)
tree1.column('codigo1', anchor='center', width=60)
tree1.column('livro', anchor='center', width=200)
tree1.column('datas', anchor='center', width=200)
tree1.place(x=-1, y=180)

# NOME
label_nome = tk.Label(alunos, text='nome', font=("arial", 17))
label_nome.place(x=5, y=10, width=90)
entry_nome = tk.Entry(alunos, font=("arial", 19))
entry_nome.place(x=90, y=10, width=600)

# TURMA
label_turma = tk.Label(alunos, text='turma', font=("arial", 17))
label_turma.place(x=5, y=50, width=90)
entry_turma = tk.Entry(alunos, font=("arial", 19))
entry_turma.place(x=90, y=50, width=600)

# código
label_codigo1 = tk.Label(alunos, text='codigo', font=("arial", 17))
label_codigo1.place(x=5, y=90, width=90)
entry_codigo1 = tk.Entry(alunos, font=("arial", 19))
entry_codigo1.place(x=90, y=90, width=570)

# BOTÃO CRIAR
botao_criar = tk.Button(alunos, text='CRIAR', bg='green', font=("arial", 15), command=adicionar_dados1)
botao_criar.place(x=5, y=130)

# BOTÃO DELETAR
botao_deletar = tk.Button(alunos, text='EXCLUIR', bg='red', font=("arial", 15), command=excluir_dados1)
botao_deletar.place(x=90, y=130)

# BOTÃO PESQUISAR
botao_pesquisar = tk.Button(alunos, text='🔎', bg='#20B2AA', font=("arial", 15), command=pesquisar_alunos)
botao_pesquisar.place(x=661, y=130)
entry_pesquisar = tk.Entry(alunos, font=("arial", 23))
entry_pesquisar.place(x=200, y=130, width=461)

# BOTÃO RENOVAR
botao_renovar = tk.Button(alunos, text='R', bg='#FF8C00', font=("arial", 13), command=renovar_livro)
botao_renovar.place(x=660, y=90, width=40)

# TREEVIEW DE LIVROS
tree2 = ttk.Treeview(livros, columns=('livro', 'genero', 'codigo'), show='headings')
tree2.heading('livro', text='livro')
tree2.heading('genero', text='genero')
tree2.heading('codigo', text='codigo')
tree2.column('livro', anchor='center', width=300)
tree2.column('genero', anchor='center', width=200)
tree2.column('codigo', anchor='center', width=200)
tree2.place(x=-1, y=180)

# Adiciona tags para estilos
style.configure("Treeview",
                background="#ffffff",
                foreground="#000000",
                fieldbackground="#ffffff")
style.map("Treeview",
          background=[("selected", "#1669f7")])

# livro
label_livro = tk.Label(livros, text='livro', font=("arial", 17))
label_livro.place(x=5, y=10, width=90)
entry_livro = tk.Entry(livros, font=("arial", 19))
entry_livro.place(x=90, y=10, width=600)

# genero
label_genero = tk.Label(livros, text='genero', font=("arial", 17))
label_genero.place(x=5, y=50, width=90)
entry_genero = tk.Entry(livros, font=("arial", 19))
entry_genero.place(x=90, y=50, width=600)

# código
label_codigo2 = tk.Label(livros, text='codigo', font=("arial", 17))
label_codigo2.place(x=5, y=90, width=90)
entry_codigo2 = tk.Entry(livros, font=("arial", 19))
entry_codigo2.place(x=90, y=90, width=600)


# BOTÃO CRIAR
botao_criar = tk.Button(livros, text='CRIAR', bg='green', font=("arial", 15), command=adicionar_dados2)
botao_criar.place(x=5, y=130)

# BOTÃO DELETAR
botao_deletar = tk.Button(livros, text='EXCLUIR', bg='red', font=("arial", 15), command=excluir_dados2)
botao_deletar.place(x=90, y=130)

# BOTÃO PESQUISAR
botao_pesquisar = tk.Button(livros, text='🔎', bg='#20B2AA', font=("arial", 15), command=pesquisar_livros)
botao_pesquisar.place(x=660, y=130)
entry_pesquisar_livros = tk.Entry(livros, font=("arial", 23))
entry_pesquisar_livros.place(x=200, y=130, width=460)

janela.mainloop()
