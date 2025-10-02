# 🤖 ChatBot Local avec Ollama & Gradio

Ce projet est un assistant conversationnel local utilisant [Ollama](https://ollama.com/) pour l’inférence de modèles LLM et [Gradio](https://gradio.app/) pour l’interface web.  
Il permet de discuter avec différents modèles IA en français, tout en sauvegardant l’historique des conversations.

---

## Fonctionnalités

- **Interface web simple** (Gradio)
- **Choix du modèle** (configurable dans `models.py`)
- **Sauvegarde automatique** de l’historique de chat
- **Effacement rapide** de l’historique
- **Support du streaming de réponses**
- **Tout fonctionne en local** (pas d’envoi de données vers l’extérieur)

---

## Prérequis

- Python 3.8+
- [Ollama](https://ollama.com/download) installé et lancé sur votre machine
- Modèles Ollama téléchargés (voir ci-dessous)

---

## Installation

1. **Cloner le dépôt**  
   ```bash
   git clone https://github.com/kamagatey/Chatbot.git
   cd ChatBot
   ```

2. **Installer les dépendances Python**  
   ```bash
   pip install gradio ollama
   ```

3. **Télécharger les modèles Ollama**  
   Par exemple :
   ```bash
   ollama pull mistral:7b-instruct-q4_K_M
   ollama pull deepseek-coder:1.3b
   ```
   *(Possibilités d'ajout de d'autre modele `models.py`)*


## Utilisation

Lancez l’interface web avec :

```bash
python app.py
```

- Accédez à [http://localhost:7860](http://localhost:7860) dans votre navigateur.
- Choisissez un modèle, tapez votre message et discutez !
- Cliquez sur **Effacer l’historique** pour repartir de zéro.

---

## Structure du projet

```
ChatBot/
│
├── app.py              # Lancement de l’interface Gradio
├── chat_logic.py       # Logique de dialogue avec Ollama
├── models.py           # Liste des modèles disponibles
├── utils.py            # Fonctions utilitaires (sauvegarde, chargement)
├── data/               # Dossiers de sauvegarde des conversations
├── .gitignore
└── README.md
```

---

## Personnalisation

- **Ajouter un modèle** :  
  Ajoutez son nom dans la liste `MODELS` du fichier `models.py` et téléchargez-le avec `ollama pull`.
---

## Notes

- Les conversations sont sauvegardées dans le dossier `data/conversations/`.
- L’historique de la dernière session est stocké dans `data/last_session.json`.
- Le projet fonctionne **uniquement en local** pour la confidentialité.

---

## Dépendances principales

- [Gradio](https://gradio.app/)
- [Ollama Python Client](https://github.com/ollama/ollama-python)

---

## Licence

Projet open-source, à adapter selon vos besoins.
**KAMAGATE YOUSSOUF**
