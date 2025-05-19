from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is the second Flask app in the lab roadmap!"


if __name__ == "__main__":
    app.run(debug=True)

    