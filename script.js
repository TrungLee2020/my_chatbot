// script.js
document.getElementById('send-button').addEventListener('click', () => {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    const chatBox = document.getElementById('chat-box');
    const userMessage = document.createElement('div');
    userMessage.textContent = `You: ${userInput}`;
    chatBox.appendChild(userMessage);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.textContent = `Bot: ${data.response}`;
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById('user-input').value = '';
});
