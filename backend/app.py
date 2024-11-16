from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')

# Enable CORS for API endpoints
CORS(app)

@app.route('/')
def serve_index():
    """
    Serves the main index.html file.
    """
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/api/hello')
def api_hello():
    """
    API endpoint that returns a "Hello, World!" message.
    """
    return jsonify(message="Hello, World!")

@app.route('/static/<path:path>')
def serve_static(path):
    """
    Serves static files like CSS or JS from the frontend/static folder.
    """
    return send_from_directory(f'{app.template_folder}/static', path)

if __name__ == '__main__':
    app.run(debug=True)
