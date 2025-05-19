from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Gavin's Flask App is working!"

if __name__ == "__main__":
    app.run(debug=True)
