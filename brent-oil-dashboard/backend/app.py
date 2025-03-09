from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from routes.analysis import analysis_bp
app.register_blueprint(analysis_bp)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Brent Oil Price Analysis API!"})

if __name__ == '__main__':
    app.run(debug=True)
