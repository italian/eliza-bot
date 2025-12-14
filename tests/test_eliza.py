import os
import sys
import unittest

# Ensure repository root is on sys.path so tests can import `eliza` when run
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import eliza


class TestEliza(unittest.TestCase):
    def test_ya_rule(self):
        resp = eliza.match_and_respond("Я грустный")
        expected = {"Почему ты грустный?", "Как давно ты грустный?"}
        self.assertIn(resp, expected)

    def test_fallback(self):
        resp = eliza.match_and_respond("Привет")
        expected = {"Расскажи подробнее.", "Интересно...", "Продолжай."}
        self.assertIn(resp, expected)

    def test_ya_hochu_rule(self):
        resp = eliza.match_and_respond("Я хочу мороженое")
        expected = {"Зачем ты хочешь мороженое?"}
        self.assertIn(resp, expected)

    def test_case_insensitive(self):
        resp = eliza.match_and_respond("я грустный")
        expected = {"Почему ты грустный?", "Как давно ты грустный?"}
        self.assertIn(resp, expected)

    def test_template_typeerror_returns_template(self):
        # Temporarily replace rules with one that will raise TypeError when
        # formatting (one captured group but template expects two placeholders).
        old_rules = eliza.rules
        try:
            eliza.rules = {r"^X (.*)": ["%s %s"]}
            resp = eliza.match_and_respond("X value")
            # On TypeError the function should return the raw template string
            self.assertEqual(resp, "%s %s")
        finally:
            eliza.rules = old_rules


if __name__ == "__main__":
    unittest.main()
