from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    output = None
    text = Translator(from_lang="english", to_lang="polish")
    if request.method == "POST":
        entry_content = request.form.get("content")
        translation = text.translate(entry_content)

        if output is None:
            output = translation
    return render_template("home.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)



