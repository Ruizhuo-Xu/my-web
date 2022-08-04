from flask import Flask, render_template


app = Flask(__name__)

@app.route("/show/info")
def show_info():
    return render_template("show_info.html")


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run()