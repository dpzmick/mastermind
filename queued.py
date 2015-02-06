from redis import Redis
import redis
from rq import Queue
from random_player import RandomPlayer
from sim import run_many_games
import time

big = Queue('big', connection=Redis())
small = Queue('small', connection=Redis())
big_jobs = []
small_jobs = []

games_per_big = 9500
games_per_small = 6000

big_hosts = 9
small_hosts = 4

games = 5000000000
#tasks = games / games_per_task

r = redis.StrictRedis("192.168.1.201", port=6379, db=0)

while r.llen('rp') < games:
    small_avail = small_hosts - len(filter(lambda x: x.result == None, small_jobs))
    big_avail = big_hosts - len(filter(lambda x: x.result == None, big_jobs))

    for i in range(0, big_avail):
        big_jobs.append(big.enqueue(run_many_games, RandomPlayer, games_per_big,
            redis_key="rp"))

    for i in range(0, small_avail):
        small_jobs.append(small.enqueue(run_many_games, RandomPlayer, games_per_small,
            redis_key="rp"))
    
    #if small_avail > 0:
    #    print "smalls: %d" % small_avail
    #if big_avail > 0:
    #    print "bigs: %d" % big_avail

print "finished"
