from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "KO(#j94usdf)sdfee3"
boggle_game = Boggle()


@app.route("/")
def home():
    session["board"] = session.get("board", boggle_game.make_board())
    session["score"] = session.get("score", 0)
    session["game-played"] = session.get("game-played", 0) + 1
    session["highest-score"] = session.get("highest-score", 0)
    return render_template("app.html", game=session["board"])


@app.route("/check_valid_word/", methods=["POST"])
def check_valididty():
    word = request.json["word"].lower()
    result = boggle_game.check_valid_word(session["board"], word)
    if result == "ok":
        session["score"] += len(word)
    session["highest-score"] = max(session["highest-score"], session["score"])
    return jsonify({"result": result})


@app.route("/new-board")
def new_baord():
    session["board"] = boggle_game.make_board()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
