from flask import Flask, render_template, request
from image import Search

app = Flask(__name__)

@app.route('/')
def index():
    search=(Search(1).getThumbs("homeless man"))
    return render_template("main.html", picture=search[0])

if __name__ == "__main__":
    app.run(debug=True)