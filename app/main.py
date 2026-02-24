import os
from flask import Flask, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel

app = Flask(__name__)
project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "rishabh-genai-gateway-123")
vertexai.init(project=project_id, location="us-east4")
model = GenerativeModel("gemini-1.5-pro")

@app.route("/", methods=["POST", "GET"])
def generate():
    if request.method == "GET":
        return "Hello GenAI is running on GKE via the Gateway API!"
    data = request.json
    prompt = data.get("prompt", "Say hello!")
    response = model.generate_content(prompt)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
