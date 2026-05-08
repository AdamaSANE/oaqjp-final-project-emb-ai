"""
Ce module implémente un serveur Flask pour la détection d'émotions.
Il reçoit du texte via une interface web et utilise le package
EmotionDetection pour analyser les sentiments.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Récupère le texte depuis les arguments de la requête, 
    analyse les émotions et renvoie le résultat formaté.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Texte invalide ! Veuillez réessayer !"

    return (
        f"Pour l'énoncé donné, la réponse du système est 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} et 'sadness': {response['sadness']}. "
        f"L'émotion dominante est {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Cette fonction gère le rendu de la page d'accueil de l'application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)