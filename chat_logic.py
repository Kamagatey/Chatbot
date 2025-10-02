from ollama import Client
from utils import save_chat_state
import time

client = Client(host="http://localhost:11434", timeout=120)

def discuter_stream(message, chat_history, model, max_tokens=500):
    messages = [{"role": "system", "content": "Réponds en français."}]
    
    try:
        # Conserve seulement les 4 derniers échanges(stockage limité)
        messages.extend({
            "role": turn["role"],
            "content": turn["content"][:500]
        } for turn in chat_history[-4:])
        
        messages.append({"role": "user", "content": message[:500]})

        stream = client.chat(
            model=model,
            messages=messages,
            stream=True,
            options={
                "num_predict": max_tokens,
                "temperature": 0.7,
                "seed": 42
            }
        )
        
        full_response = ""
        start_time = time.time()
        
        for chunk in stream:
            if time.time() - start_time > 60:
                raise TimeoutError("Délai dépassé")
            token = chunk["message"]["content"]
            full_response += token
            yield chat_history + [
                {"role": "user", "content": message},
                {"role": "assistant", "content": full_response}
            ], "", model

        # Sauvegarde finale
        final_history = chat_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": full_response}
        ]
        save_chat_state(final_history)
        yield final_history, "", model

    except Exception as e:
        error_msg = f"Erreur Ollama: {str(e)[:100]}"
        yield chat_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": error_msg}
        ], "", model
