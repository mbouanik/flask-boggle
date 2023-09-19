from unittest import TestCase
from app import app
from flask import session, jsonify
from boggle import Boggle


class FlaskTests(TestCase):
    # TODO -- write tests for every view function / feature!
    def test_home(self):
        with app.test_client() as client:
            res = client.get("/")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(session.get("board", [])), 5)
            self.assertEqual(session["game-played"], 0)
            self.assertEqual(session["highest-score"], 0)

    def test_valid_word(self):
        with app.test_client() as client:
            client.get("/")
            res = client.post("/check-word", data={"word": "dfldskj"})
            self.assertEqual(res, "not-a-word")

    def test_new_board(self):
        with app.test_client() as client:
            res = client.get("/new-board")
            self.assertEqual(302, res.status_code)
            self.assertEqual(len(session["board"]), 5)

    def test_end_of_game(self):
        with app.test_client() as client:
            self.assertEqual(res.status_code, 200)
            res = client.get("/")

            res = client.post("/end-of-game", data={"score": 23})

            self.assertEqual(session["game-played"], 0)
            # self.assertEqual(session["highest-score"], 23)
            # self.assertIn(data, "1")
            # self.assertEqual(res.data, "application/json")
