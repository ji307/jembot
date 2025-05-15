from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Ta clé OpenAI doit être stockée dans les variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Jembot est en ligne !"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    history = data.get("history", [])
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=history,
            max_tokens=500,
            temperature=0.7,
        )
        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
