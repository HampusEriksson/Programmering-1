import random

wr = 0.4
matches = 100
over80 = 0

for i in range(1000):
    wins = 0
    for j in range(matches):
        if random.random() <= wr:
            wins += 1

    if wins >= matches * 0.8:
        over80 += 1

print(over80)
