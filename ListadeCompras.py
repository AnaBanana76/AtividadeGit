import tkinter as tk
from tkinter import ttk

def adicionar_item():
    item = entrada_produto.get()
    if item:
        lista_compras.insert(tk.END, "- " + item + "\n")
        entrada_produto.delete(0, tk.END)

def remover_item():
    item_remover = entrada_produto.get()
    linhas = lista_compras.get("1.0", tk.END).splitlines()
    lista_compras.delete("1.0", tk.END)
    for linha in linhas:
        if linha.strip() != "- " + item_remover:
            lista_compras.insert(tk.END, linha + "\n")
    entrada_produto.delete(0, tk.END)

def salvar_e_fechar():
    lista = lista_compras.get("1.0", tk.END).strip()
    print("Lista de Compras:\n", lista)
    janela.destroy()

janela = tk.Tk()
janela.configure(bg="#aadfe6")
janela.title("Lista de Compras")
janela.geometry("300x400")

label_produto = tk.Label(janela, text="Produto:", bg='#aadfe6', font=("Forte",20))
label_produto.grid(row=0, column=0, padx=2, pady=5, sticky='ew')

entrada_produto = tk.Entry(janela, relief="solid")
entrada_produto.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

botao_adicionar = tk.Button(janela, text="Adicionar", fg="white", command=adicionar_item, bg='#7f70c2')
botao_adicionar.grid(row=2, column=0, padx=10, pady=5, sticky='e')

label_lista = tk.Label(janela, text="Lista de Compras:", bg='#aadfe6', font=("Forte",20))
label_lista.grid(row=3, column=0, padx=2, pady=2, sticky='ew')

lista_compras = tk.Text(janela, relief="solid")
lista_compras.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')
janela.grid_rowconfigure(4, weight=1)
janela.grid_columnconfigure(0, weight=1)

frame_botoes_inferior = tk.Frame(janela, bg="#aadfe6")
frame_botoes_inferior.grid(row=5, column=0, padx=10, pady=5, sticky='e')

botao_remover = tk.Button(frame_botoes_inferior, text="Remover", command=remover_item, bg='#cf5757', fg='white')
botao_remover.pack(side='left', padx=5)

botao_salvar_fechar = tk.Button(frame_botoes_inferior, text="Salvar e Fechar", command=salvar_e_fechar, bg='#61cf57', fg='white')
botao_salvar_fechar.pack(side='left', padx=5)

janela.mainloop()