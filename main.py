from flask import Flask, render_template

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Cria a rota principal do site
@app.route('/')
def home():
    # Renderiza o arquivo index.html que deve estar na pasta 'templates'
    return render_template('index.html')

if __name__ == '__main__':
    # Roda o servidor no modo debug, facilitando ver os erros e atualizações em tempo real
    app.run(debug=True)