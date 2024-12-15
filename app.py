from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'São Paulo Vazia.html')

# Route to serve static files (images)
@app.route('/fotos/<path:filename>')
def serve_images(filename):
    return send_from_directory('fotos', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 