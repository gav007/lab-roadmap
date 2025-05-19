from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = html.escape(request.form.get("name"))
        message = html.escape(request.form.get("message"))
        return f"<h2>Thanks, {name}!!</h2><p>Your Message:</p><p>{message}</p>"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
