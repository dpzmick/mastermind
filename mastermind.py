from random import randint
from copy import deepcopy, copy

class Mastermind:
    def __init__(self, positions=4, colors=6, code=None):
        self.positions = positions
        self.colors = colors

        if code is None:
            code = self.random_code()
        else:
            if not self.is_code_valid(code):
                raise Exception("Not a valid code!")

        self.code = {}
        for color in range(1, self.colors + 1):
            self.code[color] = [p for p, c in enumerate(code) if c == color]

    def random_code(self):
        code = []
        for i in range(0, self.positions):
            code.append(randint(1,self.colors))
        return code
    
    def check_guess(self, guess):
        code_copy = deepcopy(self.code)
        correct = 0
        wrong_location = 0
        for p, c in enumerate(copy(guess)):
            if p in code_copy[c]:
                correct += 1
                code_copy[c].remove(p)
                guess.remove(c)

        for p, c in enumerate(guess):
            if len(code_copy[c]) > 0:
                wrong_location += 1
                code_copy[c].pop()

        return (correct, wrong_location)

    def is_code_valid(self, code):
        valid_colors = True
        for c in code:
            if c > self.colors:
                valid_colors = False
                break
        valid_colors = valid_colors and len(set(code)) <= self.colors
        return len(code) == self.positions and valid_colors

def game():
    mastermind = Mastermind()
    output = (0,0)
    turn = 0
    while output != (4,0):
        turn += 1
        print "[%d] Please enter a guess." % turn
        guess = []
        for i in range(0,mastermind.positions):
            print "guess[%d]: " % i,
            guess.append(int(raw_input()))

        print "Your guess was: " + str(guess)

        output = mastermind.check_guess(guess)

        print "%d are correct" % output[0]
        print "%d are the right color, but in the wrong place" % output[1]
    print "Yay! You got it in %d turns" % turn

if __name__ == "__main__":
    game()
