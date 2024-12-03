from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    cats = [
        {"name": "Whiskers", "img": "images/cat1.jpg", "info": "A playful tabby cat."},
        {"name": "Snowball", "img": "images/cat2.jpg", "info": "A lovely white cat."},
        {"name": "Shadow", "img": "images/cat3.jpg", "info": "A mysterious black cat."}
    ]
    return render_template("index.html", cats=cats)

if __name__ == "__main__":
    app.run(debug=True)