from unittest import TestCase
from app import app
from flask import session, jsonify
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self) -> None:
        app.config["TESTING"] = True

    def test_home(self):
        with app.test_client() as client:
            res = client.get("/")
            data = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("60", data)
            self.assertEqual(len(session.get("board", [])), 5)
            self.assertEqual(session["game-played"], 0)
            self.assertEqual(session["highest-score"], 0)

    def test_valid_word(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["board"] = [
                    ["F", "O", "R", "C", "E"],
                    ["F", "O", "R", "C", "E"],
                    ["F", "O", "R", "C", "E"],
                    ["F", "O", "R", "C", "E"],
                    ["F", "O", "R", "C", "E"],
                ]
            res = client.get("/check-word?word=ewrw")
            self.assertEqual(res.json["result"], "not-a-word")
            res = client.get("/check-word?word=force")
            self.assertEqual(res.json["result"], "ok")
            res = client.get("/check-word?word=front")
            self.assertEqual(res.json["result"], "not-on-board")

    def test_new_board(self):
        with app.test_client() as client:
            res = client.get("/new-board")
            self.assertEqual(302, res.status_code)
            self.assertEqual(len(session["board"]), 5)

    def test_end_of_game(self):
        with app.test_client() as client:
            res = client.get("/end-of-game?score=23")

            self.assertEqual(session["game-played"], 1)
            # self.assertEqual(session["highest-score"], 23)
            # self.assertIn(data, "1")
            # self.assertEqual(res.data, "application/json")
