from matplotlib import pyplot as plt
from problem_class import Problem
import json
import requests

url = 'https://codeforces.com/api/problemset.problems'
json_data = requests.get(url).json()

# All problems will be stored in this list
problems_list = []


# Get all the problems information from json and store it in the list
for problem in json_data['result']['problems']:
    prblm = Problem(str(problem['contestId']) + problem['index'],
                    problem['name'],
                    problem['rating'] if 'rating' in problem else None,
                    problem['tags'],
                    )
    problems_list.append(prblm)

# Separately find the number of solves for every problem (stored as another object in json)
for i, problem in enumerate(json_data['result']['problemStatistics'], start=0):
    problems_list[i].solved_cnt = problem['solvedCount'] if 'solvedCount' in problem else None


solved_by_difficulty = [0] * 28  # number of solved problems of every difficulty
difficulties = [0] * 28  # list of difficulties (800 - 3500)
for i in range(len(difficulties)):
    difficulties[i] = 800 + i * 100

for problem in problems_list:
    if problem.difficulty and problem.solved_cnt:
        solved_by_difficulty[int((problem.difficulty - 800) / 100)] += problem.solved_cnt
    else:
        continue


# lists of coordinates where ticks will be placed
x = [800, 1100, 1400, 1700, 2000, 2300, 2600, 2900, 3200, 3500]
y = [2000000, 4000000, 6000000, 8000000, 10000000, 12000000]

plt.bar(difficulties, solved_by_difficulty, 100)
plt.xlabel('Difficulty')
plt.ylabel('Number of solves')
plt.xticks(x)
plt.yticks(y)

plt.savefig('Graph.png')
plt.show()
