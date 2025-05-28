from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde cualquier origen (Flutter)

# Palabras clave sospechosas
keywords = [
    "urgente", "bloqueo", "verifica", "ganaste", "clic",
    "premio", "pago", "reclama", "link"
]

@app.route('/analyze', methods=['POST'])
def analyze_sms():
    data = request.get_json()
    content = data.get("message", "").lower()

    has_link = bool(re.search(r'https?://|bit\.ly', content))
    has_keyword = any(word in content for word in keywords)

    result = {
        "suspicious": has_link or has_keyword,
        "content": content
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
