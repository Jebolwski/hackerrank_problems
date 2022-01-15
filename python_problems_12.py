
# https://www.hackerrank.com/challenges/circular-array-rotation

def circularArrayRotation(a, k, queries):
    result = []
    k=k%n
    for q in queries:
        result.append(a[(n-k+q)%n])
    return result

# https://www.hackerrank.com/challenges/permutation-equation

def permutationEquation(p):
    result = []
    for i in range(1,len(p)+1):
        result.append(p.index(p.index(i)+1)+1)
    return result

# https://www.hackerrank.com/challenges/non-divisible-subset

def nonDivisibleSubset(k, s):
    # array = []
    # for i in range(len(s)):
    #     for j in range(i+1,len(s)):
    #         print("j :",j,"i :",i)
    #         array.append(array[i]+array[j])
    # array = list(set(array))
    # for i in array:
    #     if i%k==0 or k%i==0:
    #         array.remove(i)
    # return len(array)
    remainder = [0] * k
    for i in s:
        remainder[i%k]+=1
    
    maxnum = 0
    maxnum += min(remainder[0],1)
    
    if k%2==0:
        maxnum+=min(remainder[k//2],1)
        
    for i in range(1,k//2+1):
        if i!=k-i:
            maxnum+=max(remainder[i],remainder[k-i])
    
            
    return maxnum