from mastermind import Mastermind

class Player:
    def __init__(self, turn_limit=16, positions=4, colors=6):
    
        #self.log("starting")

        self.turn_limit = turn_limit
        self.positions = positions
        self.colors = colors

        #self.log("creating new game, pos: %d, colors: %d, random code"
        #        % (self.positions, self.colors))

        self.master = Mastermind(colors=colors, positions=positions)

    def log(self, message):
        print "[%s]: %s" % (self.__class__.__name__, message)

    # play the mastermind game 
    def game(self):
        return (False, -1)

def run_many_games(class_name, trials, output_file,
        turn_limit=16, positions=4, colors=6):

    #return 1
    output = open(output_file, 'w')
    output.write('game_number,turns,succeeded?\n')
    for i in range(1, trials + 1):
        #print "[%s] game number: %d" % (class_name, i)
        result = class_name(turn_limit=turn_limit,
                positions=positions, colors=colors).game()
        
        #print "[%s] result: %d" % (class_name, result[1])
        output.write("%d,%d,%s\n" % (i, result[1], result[0]))
    
    output.close()
    return 0
