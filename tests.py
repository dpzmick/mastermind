import unittest
from mastermind import Mastermind

class TestMastermindGame(unittest.TestCase):
    def test_constructor_pos_col(self):
        master = Mastermind(positions=4, colors=6)
        self.assertEqual(master.positions, 4)
        self.assertEqual(master.colors, 6)
    
    def test_constructor_code_rand(self):
        master = Mastermind(positions=4, colors=6)
        self.fail("TODO")

    def test_constructor_code_given(self):
        code = [1,2,3,4]
        master = Mastermind(code=code)
        self.fail("TODO")

    def test_check_guess_correct_all(self):
        code = [1,2,3,4]
        guess = [1,2,3,4]

        master = Mastermind(positions=4, colors=6, code=code)
        self.assertEqual(master.check_guess(guess), (4,0))

    def test_check_guess_wrong_all(self):
        code = [1,1,1,1]
        guess = [2,2,2,2]

        master = Mastermind(positions=4, colors=6, code=code)
        self.assertEqual(master.check_guess(guess), (0,0))

    def test_check_guess_a(self):
        code = [1,2,3,4]
        guess = [4,3,2,1]

        master = Mastermind(positions=4, colors=6, code=code)
        self.assertEqual(master.check_guess(guess), (0,4))

    def test_check_guess_b(self):
        code = [1,1,2,2]
        guess = [2,2,5,5]

        master = Mastermind(positions=4, colors=6, code=code)
        self.assertEqual(master.check_guess(guess), (0,2))

    def test_check_guess_c(self):
        code = [1,4,4,3]
        guess = [4,4,3,2]

        master = Mastermind(positions=4, colors=6, code=code)
        self.assertEqual(master.check_guess(guess), (1,2))

if __name__=="__main__":
    unittest.main()
