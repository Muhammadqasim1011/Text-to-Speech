from flask import Flask, render_template, request, send_file
import pyttsx3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Get the text input from the user
    text = request.form['text']

    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Convert the text to speech
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    # Return the audio file to the user for download
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run()