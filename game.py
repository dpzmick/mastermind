from mastermind import Mastermind

class Game:
    def __init__(self, turn_limit=16, positions=4, colors=6, name="game"):
        # for logging
        self.name = name
    
        self.log("starting")

        self.turn_limit = turn_limit
        self.positions = positions
        self.colors = colors

        self.log("creating new game, pos: %d, colors: %d, random code"
                % (self.positions, self.colors))

        self.master = Mastermind(colors=colors, positions=positions)

    # play the mastermind game 
    def game(self):
        return (False, -1)

    def log(self, message):
        print "[%s] %s" % (self.name, message)
