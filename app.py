from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "new one now 🚀"

app.run(host="0.0.0.0", port=10000)