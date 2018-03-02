from flask import Flask, render_template, request
from image import Search
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/searchImage', methods=['POST', 'GET'])
def searchImages():
    def adj_noun(words):
        lines = [
            ("You won't believe what this " + words['adj'] + " " + words['noun'] + " does next!!!", words['adj'] + " " + words['noun']),
            ("This " + words['adj'] + " " + words['noun'] + " will make you laugh until you cry!", words['adj'] + " " + words['noun'] + " laugh"),
			(words['adj'] + " " + words['noun'] + " are Illegal?? Find out Why", words['adj'] + " " + words['noun']),
			("Check out how " + words['adj'] + " " + words['noun'] + " have changed for the better in 2018!!", words['adj'] + " " + words['noun'])
		]
        return lines
    def adv_v(words):
        lines = [
            ("How to " + words['adv'] + " your " + words['v'], words['adv'] + " " + words['v']),
            ("Donald Trump is " + words['adv'] + " " + words['v'], words['adv'] + " " + words['v']),
			("The best way to " + words['adv'] + " " + words['v'] + " this holiday season", words['adv'] + " " + words['v']),
			("The fastest way to " + words['adv'] + " " + words['v'] + " without your parents finding out!", words['adv'] + " " + words['v'])
        ]
        return lines
    formTypes = {
        "adj_noun": adj_noun,
        "adv_v": adv_v
    }
    if request.method == 'POST':
        words = request.form
        clickbaitTitle, query = random.choice(formTypes["_".join([key for key, value in words.iteritems()])](words))
        search = (Search(5).getThumbs(query))

        return render_template("answer.html", title = clickbaitTitle, items=search)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
