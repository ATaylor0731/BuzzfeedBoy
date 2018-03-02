from flask import Flask, render_template, request
from image import Search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/searchImage', methods=['POST', 'GET'])
def searchImages():
    def adj_noun(words):
        lines = [
            ("You won't believe what this " + words['adj'] + " " + words['noun'] + " does next!!!", words['adj'] + " " + words['noun']),
            ("this " + words['adj'] + " " + words['noun'] + " will make you laugh", words['adj'] + " " + words['noun'] + " laugh")
        ]
        return lines[1]
    def adv_noun(words):
        lines = [
            ("how to " + words['adv'] + " your " + words['noun'], words['adv'] + " " + words['noun']),
            ("Donald Trump is " + words['adv'] + words['noun'], words['adv'] + " " + words['noun'])
        ]
        return lines[0]
    formTypes = {
        "adj_noun": adj_noun,
        "adv_noun": adv_noun
    }
    if request.method == 'POST':
        words = request.form
        clickbaitTitle, query = formTypes["_".join([key for key, value in words.iteritems()])](words)
        search = (Search(5).getThumbs(query))

        return render_template("answer.html", title = clickbaitTitle, items=search)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
