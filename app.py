from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Inicializar el estado del juego
game_state = {
    "scene": "inicio",
    "message": "",
    "options": []
}

# Función para manejar el inicio del juego
def inicio():
    game_state["message"] = (
        "Te despiertas en una habitación desconocida. La penumbra te rodea, y solo puedes distinguir un viejo sillón en una esquina y un teléfono antiguo de disco sobre una mesita junto a la cama. No hay ventanas ni grietas. La única fuente de sonido es el teléfono, que comienza a sonar con un timbre metálico y persistente.\n\n"
        "¿Qué haces?"
    )
    game_state["options"] = [
        {"text": "Contestar el teléfono", "action": "phone"},
        {"text": "Intentar encender la luz", "action": "light"},
        {"text": "Explorar la habitación", "action": "explore"},
        {"text": "Salir del juego", "action": "exit"}
    ]

@app.route('/')
def index():
    inicio()  # Iniciar el juego
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def game_action():
    action = request.json.get('action')
    
    # Inicio del juego
    if action == 'inicio':
        inicio()

    # Acción de contestar el teléfono
    elif action == 'phone':
        game_state["message"] = (
            "Levantas el auricular con nerviosismo. Al principio, solo hay silencio al otro lado. Luego, una voz masculina y susurrante habla.\n\n"
            "Voz: 'Nunca debes confiar en lo que ves, Ernesto. Lo que ves es una ilusión creada para engañarte.'\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Preguntar quién es", "action": "ask"},
            {"text": "Decirle que te está asustando y que quieres salir", "action": "scared"},
            {"text": "Colgar el teléfono", "action": "hang"}
        ]
    
    # Acción de preguntar quién es la voz
    elif action == 'ask':
        game_state["message"] = (
            "Ernesto: '¿Cómo sabes mi nombre? ¿Quién eres?'\n\n"
            "Voz: 'En esta habitación, nadie es lo que parece. Todo está diseñado para confundirte.'\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Buscar pistas en la habitación", "action": "search"},
            {"text": "Preguntar cómo escapar", "action": "escape"},
            {"text": "Seguir preguntando quién está al otro lado", "action": "insist"},
        ]

    # Buscar pistas en la habitación
    elif action == 'search':
        game_state["message"] = (
            "Encuentras un pequeño espejo en una de las paredes. La imagen reflejada no es tu propia figura, sino la de un hombre con una expresión de horror.\n\n"
            "Voz: 'El reflejo en el espejo te muestra tu verdadero yo. El terror que ves es tu propia verdad.'\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Seguir observando el espejo", "action": "observe_mirror"},
            {"text": "Preguntar a la voz por qué el reflejo es tan inquietante", "action": "ask_mirror"},
            {"text": "Colgar el teléfono y alejarse del espejo", "action": "hang"}
        ]

    # Acción al observar el espejo
    elif action == 'observe_mirror':
        game_state["message"] = (
            "El hombre en el espejo parece moverse y tratar de hablar, pero no se oye ningún sonido. El miedo te envuelve, y las sombras en las paredes parecen cobrar vida.\n\n"
            "Voz: 'La verdad no siempre es lo que parece. El espejo solo refleja lo que deseas ocultar.'\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Enfrentar al espejo y gritar", "action": "shout_at_mirror"},
            {"text": "Colgar el teléfono y alejarse del espejo", "action": "hang"}
        ]

    # Gritar al espejo
    elif action == 'shout_at_mirror':
        game_state["message"] = (
            "Al gritarle al espejo, sientes una ola de desesperación. La habitación se desmorona y te encuentras en un vacío oscuro.\n\n"
            "Final 1: El Laberinto Interno\n\n"
            "La habitación se vacía, y entiendes que el verdadero encierro estaba en tu mente. Tu propia paranoia y miedo habían creado el lugar en el que estás atrapado. La oscuridad te rodea mientras comprendes que nunca saldrás de tu propia prisión mental."
        )
        game_state["options"] = []

    # Acción al preguntar por qué el reflejo es inquietante
    elif action == 'ask_mirror':
        game_state["message"] = (
            "La voz te dice que el reflejo es una manifestación de tus propios miedos. La verdad está en lo que no quieres ver.\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Seguir observando el espejo", "action": "observe_mirror"},
            {"text": "Colgar el teléfono y alejarse del espejo", "action": "hang"}
        ]

    # Intentar encender la luz
    elif action == 'light':
        game_state["message"] = "Intentas encender la luz, pero el interruptor parece no funcionar. La oscuridad permanece.\n\n¿Deseas intentar otra acción?"
        game_state["options"] = [
            {"text": "Intentar otra acción", "action": "inicio"}
        ]

    # Explorar la habitación
    elif action == 'explore':
        game_state["message"] = "Exploras la habitación pero no encuentras nada significativo. La oscuridad es casi total.\n\n¿Deseas intentar otra acción?"
        game_state["options"] = [
            {"text": "Intentar otra acción", "action": "inicio"}
        ]

    # Colgar el teléfono
    elif action == 'hang':
        game_state["message"] = "Cuelgas el teléfono, pero el timbre sigue sonando como una tortura constante. La habitación empieza a cambiar.\n\n¿Deseas intentar otra acción?"
        game_state["options"] = [
            {"text": "Explorar la habitación", "action": "explore"}
        ]

    # Asustarse por la voz
    elif action == 'scared':
        game_state["message"] = (
            "Le dices a la voz que te está asustando, pero el timbre sigue sonando. La habitación comienza a cambiar.\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Colgar el teléfono", "action": "hang"}
        ]

    # Preguntar cómo escapar
    elif action == 'escape':
        game_state["message"] = (
            "Voz: 'No hay respuestas fáciles aquí. Solo preguntas sin fin. La única forma de escapar es enfrentar lo que realmente eres.'\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Le pides más detalles sobre cómo enfrentar tu verdadero yo", "action": "details"},
            {"text": "Decides explorar la habitación en busca de una salida", "action": "explore"}
        ]

    # Detalles sobre enfrentar el verdadero yo
    elif action == 'details':
        game_state["message"] = (
            "Voz: 'No hay detalles simples. La realidad es un espejo distorsionado. Solo enfrentando tus miedos más profundos puedes encontrar una salida.'\n\n"
            "¿Qué haces?"
        )
        game_state["options"] = [
            {"text": "Explorar más la habitación en busca de tus miedos", "action": "explore_fears"},
            {"text": "Colgar el teléfono y buscar una salida física", "action": "hang"}
        ]

    # Explorar la habitación en busca de miedos
    elif action == 'explore_fears':
        game_state["message"] = (
            "Mientras exploras, te enfrentas a diversos objetos que parecen representaciones de tus peores temores. A medida que los enfrentas, la habitación comienza a cambiar lentamente.\n\n"
            "Final 2: El Enfrentamiento\n\n"
            "Enfrentar tus miedos te permite ver la habitación de manera diferente. Las paredes empiezan a desmoronarse, y encuentras una puerta oculta. Al abrirla, te encuentras de vuelta en tu hogar, pero el recuerdo de la experiencia te persigue, recordándote siempre tus miedos más profundos."
        )
        game_state["options"] = []

    # Salir del juego
    elif action == 'exit':
        game_state["message"] = "Has decidido salir del juego. ¡Gracias por jugar!"
        game_state["options"] = []

    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)
