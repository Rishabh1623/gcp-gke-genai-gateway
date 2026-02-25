import os
from flask import Flask, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel

app = Flask(__name__)

# Updated to your current Project ID
project_id = "genai-gateway-488421"
vertexai.init(project=project_id, location="us-central1")

# Updated to the version visible in your Model Garden
model = GenerativeModel("gemini-2.0-flash-001")

@app.route("/", methods=["POST", "GET"])
def generate():
    if request.method == "GET":
        return "Hello GenAI is running on GKE via the Gateway API!"
    
    try:
        data = request.json
        prompt = data.get("prompt", "Say hello!")
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        # This will return the actual error message to your terminal
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)