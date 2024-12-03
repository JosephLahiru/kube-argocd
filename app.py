from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

start_time = datetime.now()

@app.route("/")
def status():
    return jsonify({"project": "kube-argocd", "start_time": start_time.isoformat()})

@app.route("/hello")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
