from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import numpy as np


app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Server no ar"

@app.route('/api/v1/classification/band/lyrics', methods=['POST'])
def classify():

    file = request.json

    lyrics = file["lyrics"]
    model = joblib.load('classification_lyrics.unip')
    
    band = model.predict([lyrics])
    proba = model.predict_proba([lyrics])
    index = np.argmax(proba)

    data = { "band" : band[0], "proba" : proba[0][index]}
    response = jsonify(data)
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
