// Importa as funções necessárias do SDK do Firebase diretamente da web (CDN)
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

// As configurações exclusivas do seu projeto Firebase
const firebaseConfig = {
  apiKey: "AIzaSyBjlEa7MEire52lk655YP0uIKa7J0eddAo",
  authDomain: "aulapython-a4154.firebaseapp.com",
  projectId: "aulapython-a4154",
  storageBucket: "aulapython-a4154.firebasestorage.app",
  messagingSenderId: "917397087348",
  appId: "1:917397087348:web:3c7b2ddae76258db0c5d21",
  measurementId: "G-9L5K0TC7VY"
};

// Inicializa o Firebase com as suas configurações
const app = initializeApp(firebaseConfig);

// Inicializa o serviço de Banco de Dados (Firestore)
const db = getFirestore(app);

// --- Lógica da Interface ---

// Seleciona os elementos do HTML pelo ID
const form = document.getElementById('form-livro');
const mensagemSucesso = document.getElementById('mensagem-sucesso');
const btnSalvar = document.getElementById('btn-salvar');

// Fica "escutando" o momento em que o formulário for enviado
form.addEventListener('submit', async (evento) => {
    // Evita que a página recarregue (comportamento padrão de formulários)
    evento.preventDefault();
    
    // Altera o botão para dar um feedback visual aos alunos de que algo está acontecendo
    btnSalvar.textContent = "Salvando...";
    btnSalvar.disabled = true;

    // Captura os textos que foram digitados nos campos
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const ano = document.getElementById('ano').value;

    try {
        // Tenta adicionar um novo documento na coleção "livros" lá no Firestore
        const docRef = await addDoc(collection(db, "livros"), {
            titulo: titulo,
            autor: autor,
            anoPublicacao: parseInt(ano), // Garante que o ano seja salvo como número
            dataCadastro: new Date()      // Salva a data e hora exata do cadastro
        });
        
        // Se der certo, mostra no console do navegador (F12) o ID gerado
        console.log("Sucesso! Livro salvo com ID: ", docRef.id);
        
        // Limpa os campos para um novo cadastro
        form.reset();
        
        // Faz a mensagem verde aparecer
        mensagemSucesso.classList.remove('escondido');
        
        // Esconde a mensagem novamente após 3 segundos (3000 milissegundos)
        setTimeout(() => {
            mensagemSucesso.classList.add('escondido');
        }, 3000);

    } catch (erro) {
        // Se algo der errado (ex: banco de dados bloqueado nas regras), cai aqui
        console.error("Erro ao salvar o livro: ", erro);
        alert("Ocorreu um erro ao salvar no banco de dados. Pressione F12 e veja o Console para detalhes.");
    } finally {
        // Independente de dar certo ou errado, devolve o botão ao estado normal
        btnSalvar.textContent = "Salvar no Acervo";
        btnSalvar.disabled = false;
    }
});