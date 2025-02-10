from flask import Flask, request, jsonify
import requests
import google.generativeai as genai

app = Flask(__name__)


@app.route('/alexa', methods=['POST'])
def alexa():
    data = request.get_json()
    request_type = data['request']['type']
    shouldEndSession = False

    if request_type == "LaunchRequest":
        response_text = "Bem vindo ao Trabalho do Rafael e do Marquinhos"
        shouldEndSession = False
    elif request_type == "IntentRequest":
        intent = data['request']['intent'] 
        intent_name = intent['name']

        if intent_name == "pergunteGemini":
            slot_value = intent['slots']['topic']['value']
           
            response_text = call_ai_model(slot_value)
            print(response_text)
        else:
            response_text = "Desculpe, não entendi a sua pergunta"
            shouldEndSession = True
    elif request_type == "SessionEndedRequest":
        response_text = "Tchau!"
        shouldEndSession = True
    else:
        response_text = "Desculpa, não deu para processar sua requisição."
        shouldEndSession = True

    return jsonify({
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": response_text,
            },
            "shouldEndSession": shouldEndSession,
        },
    })

def call_ai_model(query):
    genai.configure(api_key="AIzaSyDPvjLrnnNYW1I3LpYybvXVByJFXNcYHM8")
    model = genai.GenerativeModel('gemini-pro')
    """
    Chama a api do gemini.
    """
    try:
        response = model.generate_content(query)

        if response and response.text:
            return response.text
        else:
            return jsonify({"error": "Nenhuma resposta do gemini."}), 500
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar o  Gemini API: {e}")
        return "Desculpa, não deu para processar sua requisição."

if __name__ == '__main__':
    app.run(port=5000)