from redis import Redis
from rq import Queue
from random_player import RandomPlayer
from sim import run_many_games
from time import sleep

q = Queue('high', connection=Redis())
jobs = []

workers = 7
games = 100000
games_per_worker = games / workers

print "To run %d games with %d workers, %d games / worker" % (games, workers,
        games_per_worker)

for worker in range(0, workers):
    jobs.append(q.enqueue(run_many_games, RandomPlayer, games_per_worker,
            "shared/random_player_%d.csv" % worker))

while None in [job.result for job in jobs]:
    continue

print "finished"
