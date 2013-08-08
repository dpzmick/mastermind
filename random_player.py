from sim import Player, run_many_games
from random import randint

class RandomPlayer(Player):
    def game(self):
        for turn in range(1, self.turn_limit + 1):
            guess = [randint(1, self.colors) for i in range(0, self.positions)]
            res = self.master.check_guess(guess)
            if res == (4,0):
                return (True, turn)
        return (False, self.turn_limit)

if __name__ == "__main__":
    run_many_games(RandomPlayer, 100000, "random_player.csv")
