from flask import Flask, render_template, request
from image import Search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/searchImage', methods=['POST', 'GET'])
def searchImages():
    if request.method == 'POST':
        words = request.form
        clickbaitTitle = "You won't believe what this " + words['ajv1'] + " " + words['noun1'] + " does next!!!"

        search = (Search(5).getThumbs(words['ajv1'] + " " + words['noun1']))

        return render_template("answer.html", title = clickbaitTitle, items=search)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
