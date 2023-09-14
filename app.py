from boggle import Boggle
from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "KO(#j94usdf)sdfee3"
boggle_game = Boggle()


@app.route("/")
def home():
    session["board"] = session.get("board", boggle_game.make_board())
    return render_template("app.html", game=session["board"])


@app.route("/check_valid_word", methods=["POST"])
def check_valididty():
    word = request.form.get("word")
    if boggle_game.check_valid_word(session["board"], word) == "ok":
        print(word)
    else:
        print("Oh noooooooo!")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
