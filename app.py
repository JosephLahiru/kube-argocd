from flask import Flask, jsonify
from datetime import datetime
from waitress import serve

app = Flask(__name__)

start_time = datetime.now()


@app.route("/")
def status():
    print("processing status")
    return jsonify({"project": "kube-argocd", "start_time": start_time.isoformat()})


@app.route("/hello")
def hello_world():
    print("processing hello")
    return "Hello, World! \nThis is a Print Test!!!\nThis is my Second Test!!!"


if __name__ == "__main__":
    print("API STARTED")
    serve(app, host="0.0.0.0", port=5000)
