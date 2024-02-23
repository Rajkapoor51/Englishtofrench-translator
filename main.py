from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        # Check if request body is missing or not in JSON format
        if not request.json or 'text' not in request.json:
            return jsonify({'error': 'Invalid request format. Please provide data with a "text" key.'}), 400
        
        # Get the text to be translated from the request body
        text_to_translate = request.json['text']
        
        # Translate the text from English to French
        translator = Translator()
        translated_text = translator.translate(text_to_translate, dest='fr').text
        
        # Respond with the translated text
        response = {'translation': translated_text}
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': 'An error occurred during translation: {}'.format(str(e))}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)