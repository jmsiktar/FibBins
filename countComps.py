import math

#using F_0 = 1, F_1 = 1, F_2 = 2, ...

def listFib(k): #lists the Fibonacci numbers up to the kth one when k >= 3,
    #except for the 0 and the first 1
    assert(k >= 3)
    fibList = [1, 2]
    for i in range(3, k + 1):
        nextFib = fibList[i - 2] + fibList[i - 3]
        fibList.append(nextFib)
    return fibList

lotsOfFibs = [0, 1] + listFib(100) #global used for sake of memory storage

def indexToFib(n): #spits out index of smallest k so that F_k >= n
    if n == 0 or n == 1: return 1
    elif n == 2: return 2
    excessiveList = listFib(n + 1)
    index = 0
    while excessiveList[index] < n:
        index += 1
    return index + 1

def indexOutFib(n): #spits out index of largest k so that F_k <= n
    assert(n >= 1)
    if n == 1: return 1
    elif n == 2: return 2
    excessiveList = listFib(n + 1)
    index = 1
    while excessiveList[index] <= n:
        index += 1
    return index

def numCompositions(n): #number of compositions of n
    assert(n >= 1)
    return 2**(n - 1)

#just up to n <= 100 for sake of storage (global)
def numFibComps(n): #number of Fibonacci compositions of n
    if n == 0: return 1
    elif n == 1: return 1
    elif n == 2: return 2
    else:
        k = indexOutFib(n)
        summ = 0
        for i in range(1, k + 1):
            summ += numFibComps(n - lotsOfFibs[i + 1])
    return summ


#just up to n <= 100 for sake of storage (global)
#number of Fib comps of n only using F_m, F_{m + 1}, ...
def numFibCompsBlock(n, m):
    if n == 0: return 1
    elif n < lotsOfFibs[m + 1]: return 0
    elif n == lotsOfFibs[m + 1]: return 1
    else:
        k = indexOutFib(n)
        summ = 0
        for i in range(m, k + 1):
            summ += numFibCompsBlock(n - lotsOfFibs[i + 1], m)
    return summ

############################
#find number of ways to split n into pieces based on s's contents
#assume s is a nonempty list of positive integers written in
#decreasing order
#can also use to count FibComps by letting s be a collection of Fib numbers,
#can even delete some of the Fib numbers as we see fit!
#HOWEVER, THIS IS FOR PARTITIONS, NOT FOR COMPOSITIONS
def numPartitionsRest(n, s):
    if n == 0: return 1
    assert(len(s) >= 1)
    if(len(s) == 1): #base case
        e = s[0]
        if n % e == 0: return 1
        else: return 0
    else:
        e = s[0]
        summ = 0
        multiple = int(n/e)
        length = len(s)
        choppedList = s[1:length]
        for i in range(0, multiple + 1):
            summ += numPartitionsRest(n - e*i, choppedList)
        return summ

#number of compositions of n only using summands in s (n >= 1, s nonempty)
def numCompsRest(n, s):
    if n == 0: return 1
    assert(len(s) >= 1)
    if (len(s) == 1): #base case
        e = s[0]
        if e == n: return 1
        else: return 0
    else:
        #first purge any elements from the list that are too big
        choppedList = []
        for summand in s:
            if summand <= n:
                choppedList.append(summand)
        summ = 0 #used to add all terms together
        for summand in choppedList:
            summ += numCompsRest(n - summand, choppedList)
        
        return summ
            
#want to compare number of Fib comps of n to all comps of the same number
#that just use positive integers up to and including indexToFib(n)
def compareData1(n):
    kInt = indexToFib(n)
    listK = [i for i in range(1, kInt)]
    print("Fib Comps n = ", numFibComps(n))
    print("Restricted Comps n =", numCompsRest(n, listK))
    return None

#want to compare number of Fib comps of n using only Fibs >= F_m
#to comps using positive integers between m and int(5*n/8)
#only for m >= 4 since that's what our proof was for
def compareData2(n, m):
    listK = [i for i in range(m, int(5*n/8) + 1)]
    print("Fib Comps without first m - 1 of n =", numFibCompsBlock(n, m))
    print("Restricted Comps n =", numCompsRest(n, listK))
    return None

def runTest(): #test cases
    assert(indexToFib(3) == 3)
    assert(indexToFib(6) == 5)
    assert(indexToFib(7) == 5)

    assert(indexOutFib(7) == 4)

    assert(numFibComps(2) == 2)
    assert(numFibComps(3) == 4)
    assert(numFibComps(4) == 7)
    assert(numFibComps(5) == 14)
    assert(numFibComps(6) == 26)

    assert(numFibCompsBlock(5, 2) == 3)
    assert(numFibCompsBlock(6, 2) == 2)
    assert(numFibCompsBlock(9, 2) == 8)
    assert(numFibCompsBlock(9, 3) == 1)
    assert(numFibCompsBlock(11, 2) == 18)
    assert(numFibCompsBlock(20, 4) == 1)

    assert(numCompsRest(3, [1, 2]) == 3)
    assert(numCompsRest(3, [1, 2, 3]) == 4)
    assert(numCompsRest(4, [1, 2, 3, 4]) == 8)
    assert(numCompsRest(5, [1, 2, 3, 4]) == 15)
    assert(numCompsRest(6, [1, 2, 3, 4]) == 29)
    
    print("BAZING!")
    return None
