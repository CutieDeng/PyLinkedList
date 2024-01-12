import fastlist 
import random  

ans = fastlist.List() 

for _ in range(10000): 

    l = fastlist.List() 

    for i in range(10000):
        l.append(i)

    demos = [2, 3, 4]

    while True: 

        r = random.randrange(0, 3)
        d = demos[r] 

        total = len(l) + 1 
        total //= d 
        
        for i in reversed(range(total)): 
            l.pop(i * d) 
        
        if len(l) <= 1: 
            break 
    
    ans.append(l[0]) 

print (ans)