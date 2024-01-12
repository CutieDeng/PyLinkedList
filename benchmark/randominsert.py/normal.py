import time 
import random 
import hashlib 

m = hashlib.md5()
m.update(b"HelloWorld")
aHash = m.digest()

random.seed(aHash) 

upBound = int (1e8) 
rounds = int(2e5)

start_time = time.time()

k = [] 
for _ in range(rounds): 
    idx = random.randint(0, rounds)
    val = random.randint(0, upBound) 
    if idx <= len(k): 
        k.insert(idx, val) 
    else: 
        k.append(val) 

s = len(k)

end_time = time.time() 

print (f'Size of list: {s}')
dura = end_time - start_time 
print (f'Cost time: {dura:.2} seconds')