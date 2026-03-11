import tkinter as tk
from tkinter import messagebox
import requests

# Configurações do seu projeto Firebase
PROJECT_ID = "aulapython-a4154"
COLLECTION_NAME = "livros"

# URL da API REST do Firestore
FIRESTORE_URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/{COLLECTION_NAME}"

def salvar_livro():
    # 1. Pega os textos que o usuário digitou na interface
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()

    # Validação simples
    if not titulo or not autor or not ano:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return

    # 2. Monta o "pacote" de dados no formato que o Firestore exige
    dados = {
        "fields": {
            "titulo": {"stringValue": titulo},
            "autor": {"stringValue": autor},
            "ano": {"integerValue": ano}
        }
    }

    try:
        # 3. Faz o envio (POST) dos dados para a nuvem do Google
        resposta = requests.post(FIRESTORE_URL, json=dados)

        # Se o código de status for 200, deu tudo certo!
        if resposta.status_code == 200:
            messagebox.showinfo("Sucesso!", "O livro foi salvo no acervo com sucesso.")
            
            # Limpa os campos para o próximo cadastro
            entry_titulo.delete(0, tk.END)
            entry_autor.delete(0, tk.END)
            entry_ano.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", f"Falha ao salvar. Erro: {resposta.text}")
            
    except Exception as erro:
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar à internet: {erro}")


# ==========================================
# CONSTRUÇÃO DA INTERFACE VISUAL (TKINTER)
# ==========================================

# Cria a janela principal
janela = tk.Tk()
janela.title("Cadastro de Livros Vintage")
janela.geometry("400x350")
janela.configure(bg="#D3D3D3") # Fundo cinza claro da paleta

# Título da tela
titulo_tela = tk.Label(janela, text="Acervo de Livros", font=("Arial", 18, "bold"), bg="#D3D3D3", fg="#488399")
titulo_tela.pack(pady=20) # pady dá um espaçamento em cima e embaixo

# Campo: Título
tk.Label(janela, text="Título do Livro:", font=("Arial", 10, "bold"), bg="#D3D3D3", fg="#333333").pack(anchor="w", padx=40)
entry_titulo = tk.Entry(janela, width=35, font=("Arial", 11))
entry_titulo.pack(padx=40, pady=5)

# Campo: Autor
tk.Label(janela, text="Autor:", font=("Arial", 10, "bold"), bg="#D3D3D3", fg="#333333").pack(anchor="w", padx=40)
entry_autor = tk.Entry(janela, width=35, font=("Arial", 11))
entry_autor.pack(padx=40, pady=5)

# Campo: Ano
tk.Label(janela, text="Ano de Publicação:", font=("Arial", 10, "bold"), bg="#D3D3D3", fg="#333333").pack(anchor="w", padx=40)
entry_ano = tk.Entry(janela, width=35, font=("Arial", 11))
entry_ano.pack(padx=40, pady=5)

# Botão Salvar
btn_salvar = tk.Button(janela, text="SALVAR NO FIREBASE", font=("Arial", 11, "bold"), bg="#488399", fg="white", relief="flat", command=salvar_livro)
btn_salvar.pack(pady=25, ipadx=10, ipady=5)

# Mantém a janela aberta rodando em loop
janela.mainloop()