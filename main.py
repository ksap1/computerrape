from itertools import permutations
from string import ascii_lowercase as asci
z=[]
for i in range(1,len(asci)+1):
    for x in permutations(asci,i):
        z.append(''.join(x))
