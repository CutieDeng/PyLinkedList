import time 
import random 
import hashlib 

from linked_list import linked_list 

m = hashlib.md5()
m.update(b"HelloWorld")
aHash = m.digest()

random.seed(aHash) 

upBound = int (1e8) 
rounds = int(1e8)

start_time = time.time()

k = linked_list()
for _ in range(rounds): 
    val = random.randint(0, upBound) 
    k.append(val)

s = len(k)

end_time = time.time() 

print (f'Size of list: {s}')
dura = end_time - start_time 
print (f'Cost time: {dura:.2f} seconds')