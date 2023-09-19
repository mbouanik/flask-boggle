from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "KO(#j94usdf)sdfee3"
boggle_game = Boggle()


@app.route("/")
def home():
    """
    initiazing the home page
    board game, score, timer...
    """
    session["board"] = session.get("board", boggle_game.make_board())
    session["game-played"] = session.get("game-played", 0)
    session["highest-score"] = session.get("highest-score", 0)
    return render_template(
        "app.html",
        game=session["board"],
        highest_score=session["highest-score"],
        played=session["game-played"],
    )


@app.route("/check-word", methods=["POST"])
def check_word():
    """
    check for a valid word
    """
    print(request.json["word"])
    word = request.json["word"].lower()

    result = boggle_game.check_valid_word(session["board"], word)
    return jsonify({"result": result})


@app.route("/new-board")
def new_baord():
    """
    Create a new board
    """
    session["board"] = boggle_game.make_board()
    return redirect("/")


@app.route("/end-of-game", methods=["POST"])
def end_of_game():
    """
    check for new high score update the number of game played
    """
    res = request.json["score"]
    session["game-played"] = session.get("game-played", 0) + 1
    session["highest-score"] = max(session["highest-score"], res)
    return jsonify(
        {"played": session["game-played"], "highest-score": session["highest-score"]}
    )


if __name__ == "__main__":
    app.run(debug=True)
