from redis import Redis
from rq import Queue
from random_player import RandomPlayer
from sim import run_many_games

q = Queue('high', connection=Redis())
jobs = []

games_per_task = 2000

games = 1000000
tasks = games / games_per_task

print "Making %d tasks, %d games each, to run %d games" % (tasks,games_per_task,games)

for task in range(0, tasks):
    jobs.append(q.enqueue(run_many_games, RandomPlayer, games_per_task,
        redis_key="rp"))

while None in [job.result for job in jobs]:
    continue

print "finished"
