document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chatContainer');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');

    function addMessage(message, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        messageDiv.textContent = message;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function showLoading() {
        chatContainer.classList.add('loading');
    }

    function hideLoading() {
        chatContainer.classList.remove('loading');
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessage(message, true);
            userInput.value = '';
            showLoading();

            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            })
            .then(response => response.json())
            .then(data => {
                hideLoading();
                addMessage(data.response, false);
            })
            .catch(error => {
                hideLoading();
                addMessage('Une erreur est survenue lors de la communication avec le serveur.', false);
                console.error('Error:', error);
            });
        }
    }

    // Gestionnaire d'événements pour le bouton d'envoi
    sendButton.addEventListener('click', sendMessage);

    // Gestionnaire d'événements pour la touche Entrée
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
}); 