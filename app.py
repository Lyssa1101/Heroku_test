from flask import Flask
import os

port = int(os.environ.get("PORT"))     #nano ~/bash.bashrc ????

app = Flask(__name__)

@app.route("/")
def home():
    return "Hey there what's up world we just deployed something and python is superiorrrr"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)