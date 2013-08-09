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

def run_many_games(class_name, trials, turn_limit=16, positions=4, colors=6,
        output_file=None, redis_key=None):

    #return 1
    if not output_file == None:
        output = open(output_file, 'w')
        output.write('game_number,turns,succeeded?\n')
    if not redis_key == None:
        import redis
        r = redis.StrictRedis(host='192.168.1.201', port=6379, db=0)
    else:
        raise Exception("No output specified!")

    for i in range(1, trials + 1):
        result = class_name(turn_limit=turn_limit,
                positions=positions, colors=colors).game()
        
        if not output_file == None:
            output.write("%d,%d,%s\n" % (i, result[1], result[0]))
        if not redis_key == None:
            r.rpush(redis_key, result[1])
    
    if not output_file == None:
        output.close()

    return 0
