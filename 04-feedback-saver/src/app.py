from flask import Flask, render_template, request
import os

app = Flask(__name__)

DATA_FILE = 'feedback.txt'

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")

        with open(DATA_FILE, 'a', encoding="utf-8") as f:
            f.write(f"{name}|{message}\n")
            
    feedback_list = []

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                if "|" in line:
                    name, message = line.strip().split("|", 1)
                    feedback_list.append({"name": name, "message": message})
    return render_template("feedback.html", feedback_list=feedback_list)
            
if __name__ == "__main__":
    app.run(debug=True)
