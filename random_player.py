from game import Game
from random import randint

games = 10000

class RandomPlayer(Game):
    def __init__(self):
        Game.__init__(self, name="random_player")

    def game(self):
        for turn in range(1, self.turn_limit + 1):
            guess = [randint(1, self.colors) for i in range(0, self.positions)]
            res = self.master.check_guess(guess)
            if res == (4,0):
                return (True, turn)
        return (False, self.turn_limit)


if __name__ == "__main__":
    output = open('random_player.csv', 'w')
    output.write("game_number, turns, succeded\n")
    for i in range(1, games + 1):
        player = RandomPlayer()
        print "[random_player] Game: %d of %d" % (i, games)
        result = player.game()
        print "[random_player] result: " + str(result)
        output.write("%d, %d, %s\n" % (i, result[1], result[0]))

    output.close()
