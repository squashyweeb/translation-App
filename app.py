from flask import Flask, render_template, request, jsonify
from translate import Translator
import pyperclip

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_text = request.form['source_text']
        target_language = request.form['target_language']

        try:
            translation = translate_text_api(source_text, target_language)
            return jsonify({"translation": translation})
        except Exception as e:
            return jsonify({"error": f"Error: {e}"})

    return render_template('index.html')

def translate_text_api(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

if __name__ == '__main__':
    app.run(debug=True)
