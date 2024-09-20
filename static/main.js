document.addEventListener('DOMContentLoaded', () => {
    const messageDiv = document.getElementById('message');
    const optionsDiv = document.getElementById('options');
    const exitDiv = document.getElementById('exit');

    // Función para actualizar el mensaje y las opciones
    function updateGame(data) {
        messageDiv.textContent = data.message;
        optionsDiv.innerHTML = '';
        exitDiv.innerHTML = ''; // Limpiar el contenedor de salir

        // Crear botones para cada opción
        data.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option.text;
            button.onclick = () => sendAction(option.action);

            if (option.action === 'exit') {
                // Si es la opción de salir, añadirla al contenedor de salir
                exitDiv.appendChild(button);
            } else {
                // Añadir las demás opciones al contenedor normal
                optionsDiv.appendChild(button);
            }
        });
    }

    // Enviar la acción al servidor
    function sendAction(action) {
        fetch('/action', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action: action }),
        })
        .then(response => response.json())
        .then(data => updateGame(data))
        .catch(error => console.error('Error:', error));
    }

    // Iniciar el juego con la primera escena
    sendAction('inicio');
});
