import random
import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../app'))
from app import Guru

class TestGuruGreeting(unittest.TestCase):

    def test_greeting(self):
        expected = "Hello , I am  the Guru"
        guru = Guru()
        self.assertEqual(guru.greeting(),expected)

    def test_greeting_guru_name(self):
        expected = "Hello , I am Phil Bates the Guru"
        guru = Guru("Phil Bates")
        self.assertEqual(guru.greeting(),expected)

    def test_greeting_user_name(self):
        expected = "Hello Shakeel, I am  the Guru"
        guru = Guru()
        self.assertEqual(guru.greeting("Shakeel"),expected)

    def test_greeting_guru_and_user_names(self):
        expected = "Hello Shakeel, I am Phil Bates the Guru"
        guru = Guru("Phil Bates")
        self.assertEqual(guru.greeting("Shakeel"),expected)
        
class TestGuruQuestion(unittest.TestCase):

    def setUp(self):
        self.guru = Guru("Alistair MockLearn")

    def test_question(self):
        expected = "That is a good question, let me think about it"
        self.guru.greeting("Cheng Wei")
        self.assertEqual(self.guru.ask("Who am I?"),expected)

    def test_question_Shakeel(self):
        expected = "You cannot afford my wisdom"
        self.guru.greeting("Shakeel")
        self.assertEqual(self.guru.ask("What time is it?"),expected)

    def test_blank_question(self):
        expected = "You lazy fool, greet me before asking such a question"
        guru = Guru()
        self.assertEqual(guru.ask("What is the time?"),expected)
        

if __name__ == '__main__':
    unittest.main()
