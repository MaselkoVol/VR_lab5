from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Route for index.html
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Route for all other static files (CSS, JS, images, folders, etc.)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Change the port if needed, use debug=True for development
    app.run(host='0.0.0.0', port=5000, debug=True)
