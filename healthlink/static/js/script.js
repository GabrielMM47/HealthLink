// script.js
document.addEventListener('DOMContentLoaded', () => {
    const navbarLinks = document.querySelectorAll('#navbar a');
    const startNowButton = document.getElementById('comece-agora');
    const howItWorksButton = document.getElementById('botao-como-funciona');
    const profileIcon = document.querySelector('.perfil');
    let userLoggedIn = false; // Esta flag será usada para simular o estado de login do usuário

    // Função para simular o redirecionamento ou rolagem na página
    function navigateToSection(sectionId) {
        const section = document.querySelector(sectionId);
        section.scrollIntoView({ behavior: 'smooth' });
    }

    // Evento de clique para os links da barra de navegação
    navbarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const sectionId = link.getAttribute('href');
            navigateToSection(sectionId);
        });
    });

    // Evento de clique para o botão 'Comece Agora'
    startNowButton.addEventListener('click', () => {
        if (userLoggedIn) {
            // Redirecionar para a conversa com o chatbot (simulação)
            console.log('Redirecionando para o chatbot...');
        } else {
            // Redirecionar para a página de login/cadastro (simulação)
            console.log('Redirecionando para login/cadastro...');
        }
    });

    // Evento de clique para o botão 'Como Funciona'
    howItWorksButton.addEventListener('click', () => {
        navigateToSection('#como-funciona');
    });

    // Verificar se o usuário está logado e ajustar a interface de acordo
    function checkLoginState() {
        if (userLoggedIn) {
            document.querySelectorAll('.registro, #login').forEach(el => el.style.display = 'none');
            profileIcon.style.display = 'block';
        } else {
            document.querySelectorAll('.registro, #login').forEach(el => el.style.display = 'block');
            profileIcon.style.display = 'none';
        }
    }

    checkLoginState();

    // Aqui poderíamos adicionar mais interações e estados conforme necessário
});
