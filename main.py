from flask import Flask, render_template, request
from image import Search

app = Flask(__name__)

@app.route('/')
def index():
    search=(Search(1).getThumbs("homeless man"))
    return render_template("main.html", picture=search[0])

@app.route('/searchImage', methods=['POST', 'GET'])
def searchImages():
    if request.method == 'POST':
        words = request.form
        clickbaitTitle = "You won't believe what this " + words['ajv1'] + " " + words['noun1'] + " does next!!!"
        
        search = (Search(5).getThumbs(words['ajv1'] + " " + words['noun1']))
        
        return render_template("answer.html", title = clickbaitTitle, picture1=search[0], picture2=search[1], picture3=search[2], picture4=search[3], picture5=search[4])
    
if __name__ == "__main__":
    app.run(debug=True)