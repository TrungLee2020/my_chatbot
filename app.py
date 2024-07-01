from flask import Flask, request, jsonify
from mychatbot import Chatbot

app = Flask(__name__)

chatbot = Chatbot()
chatbot.load_data('data.json')

@app.route('/chat', method=['POST'])
def chat():
    data = request.json
    query = data['query']
    response = chatbot.get_response(query)
    return jsonify("response": response)


if __name__ == '__main__':
    app.run(debug=True)