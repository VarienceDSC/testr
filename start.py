import os
from flask import Flask, send_file
from pyngrok import ngrok

# Create a Flask app
app = Flask(__name__)

# Define the path to the user's internal storage directory
internal_storage_path = os.path.expanduser('~/storage/emulated/0/')

# Define a route to serve the files in the internal storage directory
@app.route('/<path:path>')
def serve_file(path):
    return send_file(os.path.join(internal_storage_path, path))

# Start the Flask app and ngrok tunnel
if __name__ == '__main__':
    app.run(debug=True)
    public_url = ngrok.connect(5000).public_url
    print('Public URL:', public_url)
