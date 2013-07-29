from mastermind import Mastermind
from random import randint

turn_limit = 25
games = 10000
positions = 4
colors = 6


def game():
    print "[random_player] creating new game"
    print "[random_player] pos: %d colors: %d random code" % (positions, colors)
    master = Mastermind(colors=colors, positions=positions)
    for turn in range(1, turn_limit + 1):
        guess = [randint(1, colors) for i in range(0, positions)]
        res = master.check_guess(guess)
        if res == (4,0):
            return (True, turn)

    return (False, turn_limit)


if __name__ == "__main__":
    print "random_player starting"
    output = open('random_player.csv', 'w')
    output.write("game_number, turns, succeded\n")
    for i in range(1, games + 1):
        print "[random_player] Game: %d of %d" % (i, games)
        result = game()
        print "[random_player] result: " + str(result)
        output.write("%d, %d, %s\n" % (i, result[1], result[0]))

    output.close()
