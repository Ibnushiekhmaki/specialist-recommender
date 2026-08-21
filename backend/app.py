from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Specialist Recommender API is running."

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask", "status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)