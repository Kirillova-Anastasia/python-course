from random import randint
from itertools import cycle, starmap

def randomes(seq):
    yield from starmap(randint, cycle(seq))
        
from time import time
t1 = time()
from itertools import islice
from collections import Counter 

L = (0, 11), (4, 25)
R = islice(randomes(L), 500000)

# print(sorted(Counter(R).items()))
print("".join(f"{round(v/10000)}" for k, v in sorted(Counter(R).items())))
print('Time is', time()-t1)