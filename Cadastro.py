import tkinter as tk
from tkinter import messagebox

def salvar_cadastro():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    telefone = entry_telefone.get()

    if nome == "" or idade == "" or email == "" or endereco == "" or telefone == "":
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    else:
        with open("cadastros.txt", "a") as file:
            file.write(f"Nome: {nome}, Idade: {idade}, E-mail: {email}, Endereço: {endereco}, Telefone: {telefone}\n")
        messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")

# Criando a janela principal
root = tk.Tk()
root.title("Sistema de Cadastro")

# Definindo a fonte
fonte = ("Arial", 12)

# Criando os widgets
label_nome = tk.Label(root, text="Nome:", font=fonte)
label_nome.grid(row=0, column=0, sticky="e")

entry_nome = tk.Entry(root, font=fonte)
entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

label_idade = tk.Label(root, text="Idade:", font=fonte)
label_idade.grid(row=1, column=0, sticky="e")

entry_idade = tk.Entry(root, font=fonte)
entry_idade.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

label_email = tk.Label(root, text="E-mail:", font=fonte)
label_email.grid(row=2, column=0, sticky="e")

entry_email = tk.Entry(root, font=fonte)
entry_email.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

label_endereco = tk.Label(root, text="Endereço:", font=fonte)
label_endereco.grid(row=3, column=0, sticky="e")

entry_endereco = tk.Entry(root, font=fonte)
entry_endereco.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

label_telefone = tk.Label(root, text="Telefone:", font=fonte)
label_telefone.grid(row=4, column=0, sticky="e")

entry_telefone = tk.Entry(root, font=fonte)
entry_telefone.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

button_salvar = tk.Button(root, text="Salvar Cadastro", font=fonte, command=salvar_cadastro)
button_salvar.grid(row=5, column=0, columnspan=2, pady=10)

# Centralizando a janela na tela
largura_janela = 800
altura_janela = 600
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Iniciando o loop principal da interface gráfica
root.mainloop()
