import tkinter as tk
from tkinter import messagebox, ttk # ttk é necessário para criar a tabela
import requests

# Configurações do seu projeto Firebase
PROJECT_ID = "aulapython-a4154"
COLLECTION_NAME = "livros"
FIRESTORE_URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/{COLLECTION_NAME}"

# ==========================================
# CÉREBRO: FUNÇÕES DO BANCO DE DADOS
# ==========================================

def salvar_livro():
    # 1. Captura todos os campos
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()
    editora = entry_editora.get()
    genero = entry_genero.get()
    paginas = entry_paginas.get()

    if not titulo or not autor or not ano:
        messagebox.showwarning("Aviso", "Preencha pelo menos Título, Autor e Ano!")
        return

    # 2. Monta o pacote de dados
    dados = {
        "fields": {
            "titulo": {"stringValue": titulo},
            "autor": {"stringValue": autor},
            "ano": {"integerValue": ano},
            "editora": {"stringValue": editora},
            "genero": {"stringValue": genero},
            "paginas": {"integerValue": paginas} if paginas else {"integerValue": "0"}
        }
    }

    try:
        resposta = requests.post(FIRESTORE_URL, json=dados)
        if resposta.status_code == 200:
            messagebox.showinfo("Sucesso!", "O livro foi salvo no acervo com sucesso.")
            
            # Limpa os campos
            for entry in [entry_titulo, entry_autor, entry_ano, entry_editora, entry_genero, entry_paginas]:
                entry.delete(0, tk.END)
                
            # ATUALIZA A TABELA AUTOMATICAMENTE APÓS SALVAR!
            listar_livros()
        else:
            messagebox.showerror("Erro", f"Falha ao salvar. Erro: {resposta.text}")
    except Exception as erro:
        messagebox.showerror("Erro", f"Sem internet: {erro}")

def listar_livros():
    # 1. Limpa a tabela atual antes de colocar os dados novos
    for linha in tabela.get_children():
        tabela.delete(linha)
        
    try:
        # 2. Faz o pedido (GET) para o Google para ler os dados
        resposta = requests.get(FIRESTORE_URL)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            # Pega a lista de documentos (se não tiver nenhum, pega uma lista vazia [])
            documentos = dados.get("documents", [])
            
            # 3. Passa por cada livro no banco de dados e adiciona na tabela
            for doc in documentos:
                campos = doc.get("fields", {})
                # Extrai os textos com segurança
                titulo = campos.get("titulo", {}).get("stringValue", "---")
                autor = campos.get("autor", {}).get("stringValue", "---")
                ano = campos.get("ano", {}).get("integerValue", "---")
                genero = campos.get("genero", {}).get("stringValue", "---")
                
                # Insere a linha na tabela (Treeview)
                tabela.insert("", tk.END, values=(titulo, autor, ano, genero))
        else:
            messagebox.showerror("Erro", "Não foi possível carregar o acervo.")
    except Exception as erro:
        messagebox.showerror("Erro", f"Não foi possível conectar: {erro}")

# ==========================================
# INTERFACE VISUAL (TKINTER)
# ==========================================

janela = tk.Tk()
janela.title("Painel de Controle: Acervo Vintage")
janela.geometry("900x500") # Janela bem mais larga agora!
janela.configure(bg="#D3D3D3")

# --- DIVISÃO DA TELA (FRAMES) ---
# Lado Esquerdo (Formulário)
frame_esq = tk.Frame(janela, bg="#D3D3D3", width=350)
frame_esq.pack(side="left", fill="y", padx=20, pady=20)

# Lado Direito (Tabela)
frame_dir = tk.Frame(janela, bg="#f9f9f9")
frame_dir.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# ==========================================
# LADO ESQUERDO: O FORMULÁRIO (6 Campos)
# ==========================================
tk.Label(frame_esq, text="Cadastrar Livro", font=("Arial", 16, "bold"), bg="#D3D3D3", fg="#488399").pack(pady=10)

# Campo 1
tk.Label(frame_esq, text="Título do Livro *", bg="#D3D3D3", font=("Arial", 9, "bold")).pack(anchor="w")
entry_titulo = tk.Entry(frame_esq, width=40)
entry_titulo.pack(pady=2)

# Campo 2
tk.Label(frame_esq, text="Autor *", bg="#D3D3D3", font=("Arial", 9, "bold")).pack(anchor="w", top=5)
entry_autor = tk.Entry(frame_esq, width=40)
entry_autor.pack(pady=2)

# Campo 3
tk.Label(frame_esq, text="Ano de Publicação *", bg="#D3D3D3", font=("Arial", 9, "bold")).pack(anchor="w", top=5)
entry_ano = tk.Entry(frame_esq, width=40)
entry_ano.pack(pady=2)

# Campo 4
tk.Label(frame_esq, text="Editora", bg="#D3D3D3", font=("Arial", 9, "bold")).pack(anchor="w", top=5)
entry_editora = tk.Entry(frame_esq, width=40)
entry_editora.pack(pady=2)

# Campo 5
tk.Label(frame_esq, text="Gênero Literário", bg="#D3D3D3", font=("Arial", 9, "bold")).pack(anchor="w", top=5)
entry_genero = tk.Entry(frame_esq, width=40)
entry_genero.pack(pady=2)

# Campo 6
tk.Label(frame_esq, text="Nº de Páginas", bg="#D3D3D3", font=("Arial", 9, "bold")).pack(anchor="w", top=5)
entry_paginas = tk.Entry(frame_esq, width=40)
entry_paginas.pack(pady=2)

btn_salvar = tk.Button(frame_esq, text="SALVAR", bg="#488399", fg="white", font=("Arial", 10, "bold"), command=salvar_livro)
btn_salvar.pack(pady=20, ipadx=20, ipady=5)


# ==========================================
# LADO DIREITO: A TABELA E A LISTA
# ==========================================
tk.Label(frame_dir, text="Acervo Cadastrado", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#488399").pack(pady=10)

# Configurando as colunas da tabela
colunas = ("titulo", "autor", "ano", "genero")
tabela = ttk.Treeview(frame_dir, columns=colunas, show="headings", height=15)

# Nomeando o cabeçalho de cada coluna
tabela.heading("titulo", text="Título")
tabela.heading("autor", text="Autor")
tabela.heading("ano", text="Ano")
tabela.heading("genero", text="Gênero")

# Ajustando a largura das colunas
tabela.column("titulo", width=150)
tabela.column("autor", width=120)
tabela.column("ano", width=50, anchor="center")
tabela.column("genero", width=100)

tabela.pack(fill="both", expand=True)

# Botão para atualizar a lista manualmente
btn_atualizar = tk.Button(frame_dir, text="ATUALIZAR LISTA", bg="#F4D38A", fg="#333", font=("Arial", 9, "bold"), command=listar_livros)
btn_atualizar.pack(pady=10, ipadx=10, ipady=3)

# Assim que a janela abre, ele já puxa os livros do banco de dados automaticamente!
listar_livros()

janela.mainloop()