cmd: pip install customtkinter
criação pasta do projeto
Passos do tkinter:
1. Configurar aparência
2. Criação da janela principal
3. Criação dos campos (label, entry, button)
4. Criação das funcionalidades
5. Inicia o loop da aplicação

# 📚 Cadastro de Livros Vintage (Integração Python + Firebase)

Um aplicativo simples desenvolvido em Python (Tkinter) para cadastrar livros diretamente em um banco de dados na nuvem (Google Firestore). Ideal para estudantes entenderem conceitos de interfaces gráficas e consumo de APIs REST de forma visual e prática.

---

## 💻 Parte 1: Como rodar o código-fonte (No VS Code)

Se você quer abrir o código, ler como ele funciona e rodar direto no seu computador, siga os passos abaixo:

### Pré-requisito: Instalando a biblioteca
A única coisa que você precisa instalar no terminal antes de rodar o código é a biblioteca de requisições web. 
Abra o terminal do VS Code e digite:

> `pip install requests`

*(Se der erro dizendo que o comando não é reconhecido, tente forçar a instalação com: `python -m pip install requests`)*

### Executando:
Com a biblioteca instalada, basta rodar o arquivo principal para a janela abrir:

> `python app_livros.py`

---

## 🚀 Parte 2: Como criar um Executável (.exe) do Projeto

Você pode transformar esse código em um programa "de verdade", que roda em qualquer computador com Windows sem precisar instalar o Python ou abrir o VS Code!

### Passo 1: Instalar o "Empacotador" (PyInstaller)
Vamos baixar a ferramenta que junta o seu código e a interface em um arquivo só. No terminal, digite:

> `pip install pyinstaller`

*(Se der erro de "pip não é reconhecido", use: `python -m pip install pyinstaller`)*

### Passo 2: Preparar o Ícone Personalizado (Opcional)
Para o seu programa não ficar com aquele ícone padrão e sem graça do sistema:
1. Vá no Google Imagens e procure por um ícone do seu agrado (ex: "book icon png").
2. Baixe a imagem e use um site gratuito como o [icoconvert.com](https://icoconvert.com/) para transformar em um arquivo **`.ico`**.
3. Salve esse arquivo `.ico` **dentro da mesma pasta** do seu projeto no VS Code (exemplo: `icone.ico`).

### Passo 3: O Comando Mágico (Gerando o .exe)
No mesmo terminal, digite o comando abaixo com bastante atenção:
*(Atenção: se você não baixou o ícone no passo anterior, basta apagar a parte `--icon=icone.ico`)*

> `python -m pyinstaller --onefile --windowed --icon=icone.ico app_livros.py`

**Entendendo os "Poderes" desse comando:**
* **`python -m pyinstaller`**: Garante que o Windows vai achar o empacotador sem dar erro.
* **`--onefile`**: Obriga o sistema a gerar **um único arquivo** `.exe` (muito mais fácil de levar no pen drive).
* **`--windowed`**: Impede que a tela preta de código (Console) fique aberta atrás da sua interface visual.
* **`app_livros.py`**: É o nome do arquivo principal do código.

### Passo 4: Onde está o meu programa?
O terminal vai gerar algumas pastas novas no seu projeto. 
1. Olhe na lateral esquerda do seu VS Code.
2. Procure por uma pasta chamada **`dist`** (de *Distribution*).
3. Abra essa pasta. Seu arquivo **`app_livros.exe`** estará lá dentro, pronto para uso!

Você pode copiar esse arquivo, colocar na Área de Trabalho e mandar para os amigos.

---

### 🛡️ Aviso Importante sobre Antivírus
Como esse programa foi criado por você e não possui uma assinatura digital de uma grande empresa de tecnologia, o **Windows Defender** (ou antivírus) pode exibir uma tela azul avisando que o arquivo é desconhecido na primeira vez que for aberto em outro computador. 

Não se preocupe! Basta clicar em **"Mais informações"** e depois no botão **"Executar assim mesmo"**.


# 🧠 Entendendo o Código: Aplicativo de Livros com Python

Nosso aplicativo é dividido em três grandes blocos. Pense nele como um corpo humano: temos o **Esqueleto** (configurações), o **Cérebro** (a lógica que salva os dados) e a **Pele/Rosto** (a interface visual que o usuário enxerga).

Vamos analisar cada parte do nosso arquivo `app_livros.py`.

---

## ⚙️ Parte 1: O Esqueleto (Importações e Configuração)
Antes de construir o app, precisamos trazer as ferramentas certas para a nossa mesa de trabalho e dizer para onde os dados vão.

```python
import tkinter as tk           # A ferramenta que desenha a janela e os botões
from tkinter import messagebox # A ferramenta que cria as caixinhas de aviso (sucesso/erro)
import requests                # O "carteiro" que leva nossos dados até a internet

# Configurações do seu projeto Firebase
PROJECT_ID = "aulapython-a4154"
COLLECTION_NAME = "livros"

# URL da API REST: É o "endereço postal" exato do nosso banco de dados no Google
FIRESTORE_URL = f"[https://firestore.googleapis.com/v1/projects/](https://firestore.googleapis.com/v1/projects/){PROJECT_ID}/databases/(default)/documents/{COLLECTION_NAME}"


O Cérebro (A Função de Salvar)
Esta é a função salvar_livro(). Ela fica "dormindo" até que alguém clique no botão "Salvar". Quando acordada, ela faz o trabalho pesado.

def salvar_livro():
    # 1. Captura: Pega os textos que foram digitados nas caixinhas de texto
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()

    # 2. Validação: Checa se o usuário esqueceu de preencher algo
    if not titulo or not autor or not ano:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return # Para a função aqui e não tenta salvar

    # 3. Preparação: Monta o "pacote" no formato exato que o Firestore entende
    dados = {
        "fields": {
            "titulo": {"stringValue": titulo}, # stringValue = Texto
            "autor": {"stringValue": autor},
            "ano": {"integerValue": ano}       # integerValue = Número inteiro
        }
    }

    # 4. Envio: Tenta mandar para a internet
    try:
        resposta = requests.post(FIRESTORE_URL, json=dados)

        if resposta.status_code == 200: # O código 200 na web significa "OK, deu certo!"
            messagebox.showinfo("Sucesso!", "Livro salvo no acervo com sucesso.")
            
            # Limpa as caixinhas para o próximo livro
            entry_titulo.delete(0, tk.END)
            entry_autor.delete(0, tk.END)
            entry_ano.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Falha ao salvar.")
            
    except Exception as erro: # Se o computador estiver sem internet, cai aqui
        messagebox.showerror("Erro", "Sem conexão com a internet.")


O Rosto (A Interface Visual Tkinter)
Aqui é onde nós "desenhamos" a tela linha por linha. Seguimos uma ordem lógica: criamos a janela, colocamos os textos, colocamos os campos de digitação e, por fim, o botão.

# Cria a janela base
janela = tk.Tk()
janela.title("Cadastro de Livros Vintage")
janela.geometry("400x350")      # Largura x Altura
janela.configure(bg="#D3D3D3")  # Cor de fundo

# Título Principal (Label)
titulo_tela = tk.Label(janela, text="Acervo de Livros", font=("Arial", 18, "bold"), bg="#D3D3D3", fg="#488399")
titulo_tela.pack(pady=20) 

# --- CAMPO: TÍTULO ---
# Label (o texto acima da caixinha)
tk.Label(janela, text="Título do Livro:", bg="#D3D3D3").pack(anchor="w", padx=40)
# Entry (A caixinha de digitar)
entry_titulo = tk.Entry(janela, width=35)
entry_titulo.pack(padx=40, pady=5)

# --- CAMPO: AUTOR ---
tk.Label(janela, text="Autor:", bg="#D3D3D3").pack(anchor="w", padx=40)
entry_autor = tk.Entry(janela, width=35)
entry_autor.pack(padx=40, pady=5)

# --- CAMPO: ANO ---
tk.Label(janela, text="Ano de Publicação:", bg="#D3D3D3").pack(anchor="w", padx=40)
entry_ano = tk.Entry(janela, width=35)
entry_ano.pack(padx=40, pady=5)

# --- BOTÃO DE SALVAR ---
# O parâmetro command=salvar_livro é o que conecta este botão ao nosso "cérebro" lá de cima!
btn_salvar = tk.Button(janela, text="SALVAR", bg="#488399", fg="white", command=salvar_livro)
btn_salvar.pack(pady=25, ipadx=10, ipady=5)

# O loop principal que mantém a janela aberta
janela.mainloop()

---

Desafio Prático: Como adicionar um novo campo?
E se quisermos adicionar a "Editora" do livro? Precisamos modificar o código em duas partes: na Interface (para o usuário digitar) e na Função (para salvar no banco).

Passo 1: Adicionar na Interface (Lá embaixo no código)
Logo abaixo do campo "Ano de Publicação", você deve criar a caixinha da Editora:

# --- CAMPO: EDITORA ---
tk.Label(janela, text="Editora:", bg="#D3D3D3", font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
entry_editora = tk.Entry(janela, width=35, font=("Arial", 11))
entry_editora.pack(padx=40, pady=5)

(Dica: Lembre-se de aumentar o tamanho da janela de 400x350 para algo como 400x420 em janela.geometry para caber o novo campo!)

Passo 2: Atualizar a Função de Salvar (Lá em cima no código)
Dentro da função salvar_livro(), nós precisamos capturar essa nova informação e colocá-la no "pacote" que vai para a internet.

# 1. Capture a variável
    editora = entry_editora.get() 

    # 2. Adicione na validação
    if not titulo or not autor or not ano or not editora:
        ...

    # 3. Coloque no pacote de dados (como a editora é texto, usamos stringValue)
    dados = {
        "fields": {
            "titulo": {"stringValue": titulo},
            "autor": {"stringValue": autor},
            "ano": {"integerValue": ano},
            "editora": {"stringValue": editora} # <- NOVO CAMPO AQUI
        }
    }

Não se esqueça também de limpar o campo no final da função adicionando entry_editora.delete(0, tk.END) junto com os outros!


O executável criado pelo PyInstaller funciona como uma "fotografia" do seu código. No momento em que você roda o comando, ele empacota tudo do jeito exato que estava ali e "fecha a caixa".

Se você for no seu arquivo app_livros.py, mudar a cor de um botão, salvar e dar dois cliques no .exe antigo, nada vai mudar. O executável é independente e não lê mais o seu arquivo .py depois de pronto.

Como atualizar o seu programa:
O processo é super direto:

Salve as alterações que você fez no arquivo app_livros.py.

Abra o terminal no VS Code.

Rode exatamente o mesmo comando que usamos antes:
python -m pyinstaller --onefile --windowed --icon=icone.ico app_livros.py

O sistema vai processar tudo novamente, perguntar se você deseja sobrescrever os dados antigos (basta digitar Y para Yes e dar Enter) e vai substituir o .exe que estava lá na pasta dist pela sua versão mais recente.
