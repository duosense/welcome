from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import bigquery, storage

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

@app.route('/')
def home():
    return "Hello, Flask is running!"

@app.route('/upload', methods=['POST'])
def upload_file():
    # Example endpoint to handle file uploads (for Cloud Storage)
    file = request.files['file']
    client = storage.Client()
    bucket = client.bucket('your-bucket-name')
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)
    return jsonify({'message': 'File uploaded successfully'})

if __name__ == "__main__":
    app.run(debug=True)
