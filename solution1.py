import random

def solution(N,A):
    
    #initialize "counters" with zeors
    counters=[0 for x in range (N)]
    
    for x in A:
        if x >= 1 and x <= N :
            #increase counter by 1
            counters[x-1] += 1
            
        elif x == N+1:
            #set all counters to max of all counters
            counters = [max(counters) for x in counters]
       
  
    return counters
    
N=0
M=0
while True :
    N = int(input("enter --- N --- between 1 and 100000  "))
    M = int(input("enter --- M --- between 1 and 100000  "))
    if N>=1 and N<=100000 and M>=1 and M<=100000:
        break
    print("out of RANGE --- ENTER numbers again")


A = [random.randrange(1, N+2) for x in range(M)]

res = solution(N,A)

print(res)
#
#
#
#
#
#       
#
#
#
##### Mahdi Arfaoui #####  