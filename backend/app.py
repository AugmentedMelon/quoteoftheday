from flask import Flask, jsonify
from flask_cors import CORS
import random

from waitress import serve

app = Flask(__name__)
CORS(app)

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson"
]

@app.route("/quote", methods=["GET"])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)

from app import app  # Assuming your Flask app is called `app`

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
