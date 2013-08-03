from mastermind import Mastermind

turn_limit = 16
games = 10
positions = 4
colors = 6

def game():
    print "[knuth_player] creating new game"
    print "[knuth_player] pos: %d, colors: %d, random code" % (positions,
            colors)
    possibles = colors ** positions
    print "[knuth_player] %d possible combos" % possibles
    master = Mastermind(colors=colors, positions=positions)
    
if __name__ == "__main__":
    print "knuth_player starting"
    output = open('knuth_player.csv', 'w')
    output.write('game_number, turns, succeded\n')
    for i in range(1, games + 1):
        print "[knuth_player] Game: %d of %d" % (i, games)
        result = game()
