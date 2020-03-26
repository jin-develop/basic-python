import time
import random

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    start_time = time.time()
    user_input = str(input(q + '|n')).strip()
    end_time = time.time() = start_time

    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c ==q[i]:
            correct += 1
    tot_len = len(q)
    c = correct / tot_len * 100
    e = tot_len 

