import gradio as gr
from chat_logic import discuter_stream
from models import MODELS
from utils import load_chat_state

# Charger l’historique précédent
initial_history = load_chat_state()

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Assistant Local")

    with gr.Row():
        modele = gr.Dropdown(label="🧠 Choisir un modèle", choices=MODELS, value=MODELS[0])
        bouton_clear = gr.Button("🔁 Effacer l’historique")

    chatbot = gr.Chatbot(label="Assistant", height=500, type='messages')
    message = gr.Textbox(show_label=False, placeholder="💬 Entrez votre message...", lines=2)

    envoyer = gr.Button("📤 Envoyer")

    # Mémoire de chat
    chat_state = gr.State(initial_history)

    # Ici on appelle directement discuter_stream (plus besoin de dispatcher)
    message.submit(discuter_stream, [message, chat_state, modele], [chatbot, message, modele])
    envoyer.click(discuter_stream, [message, chat_state, modele], [chatbot, message, modele])

    # Reset conversation
    bouton_clear.click(lambda: [], None, chatbot).then(lambda: [], None, chat_state)

demo.launch(share=False, server_name="0.0.0.0", server_port=7860, inbrowser=True)
