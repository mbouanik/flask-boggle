from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "KO(#j94usdf)sdfee3"
boggle_game = Boggle()


@app.route("/")
def home():
    session["board"] = session.get("board", boggle_game.make_board())
    session["game-played"] = session.get("game-played", 0)
    session["highest-score"] = session.get("highest-score", 0)
    return render_template(
        "app.html",
        game=session["board"],
        highest_score=session["highest-score"],
        played=session["game-played"],
    )


@app.route("/check_valid_word/", methods=["POST"])
def check_valididty():
    word = request.json["word"].lower()
    print(word)
    result = boggle_game.check_valid_word(session["board"], word)
    return jsonify({"result": result})


@app.route("/new-board")
def new_baord():
    session["board"] = boggle_game.make_board()
    return redirect("/")


@app.route("/end-of-game", methods=["POST"])
def end_of_game():
    res = int(request.json["score"])
    print(res)
    session["game-played"] = session["game-played"] + 1
    session["highest-score"] = max(session["highest-score"], res)
    return jsonify(
        {"played": session["game-played"], "highest-score": session["highest-score"]}
    )


if __name__ == "__main__":
    app.run(debug=True)
