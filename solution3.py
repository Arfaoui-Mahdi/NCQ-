#logic is simple, for a giving array A, if A[i]>0 and A[i+1]>0 , we'll substract them
#that mean S[i]=1 and S[i+1] = -1 , if A[i]<0 and A[i+1]>0 (or inverse) we'll add them (their S[index]
# will be equal to 1), here's an example :

# A = [ -2   ,   2   ,   4   ,   6   ,  -10  ,   8   ]
#        \   +  /
#       S[0]=S[1] = 1              
#           \ /
#    [       0       ,   4   ,   6   ,  -10  ,   8   ]          S = [1,1]       
#               \   -  /         
#              S[i+1]=-1 (if A[i+2]<0 esle = -1 , here we have A[i+2]=6 > 0 then S[i+1]=-1)
#                  \ /
#    [       0  ,   -4    ,      6   ,     -10  ,     8   ]     S = [1,1,-1]          
#                      \   +  /
#                   S[i+1] = 1
#                         \ /
#    [      0  ,   -4   ,  2       ,     -10  ,     8   ]     S = [1,1,-1,1]          
#                               \   +  /
#                              S[i+1] = 1
#                                  \ /
#    [      0  ,   -4   ,  2        -8   ,    8   ]     S = [1,1,-1,1,1]    
#                                     \   +  /
#                                    S[i+1] = 1
#                                         \ /
#    [      0  ,   -4   ,  2        -8,    0   ]     S = [1,1,-1,1,1,1]  
#                                          ^ 
#                                          |
#                                          |  
#and finally we have our S array with the last element of our working array = 0 (min possible value)
import random

def oppSign(x,y):
    return ((x ^ y) < 0) # True == opposite , False == not oppsite 


def solution(A):
    workArr = [0 for x in range (len(A)-1)]
    S = [0 for x in range (len(A))]

   
            
   
    for i in range(1,len(A)):
        #initialze S and workArr to work with them later
        if i-1 == 0 : 
            if oppSign(A[i-1] , A[i]) :
                S[i-1] = 1
                S[i] = 1
            else : 
                S[i-1] = -1
                S[i] = 1

            if A[i-1] == 0 :
                S[i-1] = 1
            
            if A[i] == 0 :
                S[i] = 1
            
            workArr[0] = A[0] * S[0] + A[1] * S[1]
        
        #handle the rest of values
        else : #from i = 2
            if oppSign (workArr[i-2] , A[i]) or A[i] == 0:
                S[i] = 1
                workArr[i-1] = workArr[i-2] + A[i] * S[i]
            else :
                S[i] = -1
                workArr[i-1] = workArr[i-2] + A[i] * S[i]

    
    res = abs(workArr[len(A)-2]) #since distance is always positive, we assign abs of last value
    return res
    #return res,S  #uncomment this line to see the S Array along side with our main result


while True :
    N = int(input("enter a numebr between 0 and 20000  :  "))
    if N>=0 and N<=20000:
        break
    print("OUT-OF-RANGE : enter a correct numebr")

A = [random.randrange(-101, 101) for x in range(N)]
#print(A) #uncomment to see the values we'll work with
print(solution(A))
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
        






