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
