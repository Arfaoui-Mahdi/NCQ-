# it is obvious that there is a repeated work happening to get the number of ways to climb
#the ladder with 1 or 2 stpes, it is a recursion problem, and the recursion lays in the fact 
#that we could determine reach i'th rung either from i-1 or i-2 so we have : n_ways(n)=n_ways(n-1)+n_ways(n-2)
#for exemple n_ways(4)= 5 (in the given exemple) and n_ways(3) = 3 ([1,1,1],[1,2],[2,1]) then
#n_ways(5) = n_ways(4)+n_ways(3) = 8 (proved in the given exemple)
#we could use recursion but you told us to use the most optimized way possible
#that's why i'll use Dynamic Programming to do not repeat the same process in recursion technique and 
#store the local results in a temporary array
import random


def cal_N_Ways(n): 
    
    #creates array n_ways with all elements = 0 
    n_ways = [0 for x in range(n)]  
    n_ways[0], n_ways[1] = 1, 1 #since fisrt step has only one way 
      
    for i in range(2, n): 
        j = 1
        while j<= 2 and j<= i: 
            n_ways[i] = n_ways[i] + n_ways[i-j] #store the result of i'th rung in n_ways ==> n_ways[lastIndex] is our result
            j = j + 1 
    return n_ways[n-1] #lastIndex = n-1
  


def solution(A,B):
    N = len(A)
    res=[]
    for i in range (N) :
        numWays = cal_N_Ways(A[i]+1)
        inc = numWays % (2**B[i])
        res.append(inc)
    
    return res

while True :
    L = int(input("enter a numebr between 0 and 50000  :  "))
    if L >=0 and L<=20000:
        break
    print("OUT-OF-RANGE : enter a correct numebr")


A = [random.randrange(1,L+1) for x in range(L)]
B = [random.randrange(1,30+1) for x in range(L)]


print(solution(A,B))
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



      


