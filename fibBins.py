#find number of ways to split n into
#some number of nonempty bins so each bin has a Fibonacci Number of balls
#will be easy to sift and subtract configs with some bins having a min capacity
from itertools import permutations
import math
phi = (1 + math.sqrt(5))/2
psi = (1 - math.sqrt(5))/2

####HELPER FUNCTIONS/ILLUSTRATIONS#######

def permu(): #generate a set of all permutations example
    l = set(permutations(range(1, 4)))
    print(l)

def listLucas(k): #lists the Lucas numbers up to the kth one when k >= 2
    assert(k >= 2)
    lucasList = [2, 1]
    for i in range(2, k + 1):
        nextLucas = lucasList[i - 1] + lucasList[i - 2]
        lucasList.append(nextLucas)
    return lucasList

def listFib(k): #lists the Fibonacci numbers up to the kth one when k >= 3,
    #except for the 0 and the first 1
    assert(k >= 3)
    fibList = [1, 2]
    for i in range(3, k + 1):
        nextFib = fibList[i - 2] + fibList[i - 3]
        fibList.append(nextFib)
    return fibList

def listFibFilterMod(k, n): #lists the Fibonacci numbers up to the kth one when k >= 3,
    #except for the 0 and the first 1, and all of those which are divisible by n
    fibList = listFib(k)
    assert(n >= 2)
    if n == 2:
        filterList = [1]
    else:
        filterList = [1, 2]
    for i in range(3, k + 1):
        nextFib = fibList[i - 2] + fibList[i - 3]
        if nextFib % n != 0:
            filterList.append(nextFib)
    return filterList

def kthFib(k): #gives the kth Fibonacci number when k >= 3
    assert(k >= 3)
    possibleFibs = listFib(k)
    numInList = len(possibleFibs)
    return possibleFibs[numInList - 1]

def listSmallFibs(n): #list all Fibonacci Numbers <= n starting from the second 1
    assert(n >= 1)
    fibList = [1]
    if n == 1: return fibList
    fibList.append(2)
    largestFib = 2
    secondLargest = 1
    while n > largestFib:
        newLargest = largestFib + secondLargest
        secondLargest = largestFib
        largestFib = newLargest
        fibList.append(newLargest)
    if n < largestFib:
        fibList.pop() #removes last element
    return fibList

def listSmallLucas(n): #list all Lucas Numbers <= n starting from 2, 1, 3...
    #assert(n >= 2)
    if n == 1: return [1]
    lucasList = [2, 1]
    if n == 2: return lucasList
    lucasList.append(3)
    largestLucas = 3
    secondLargest = 1
    while n > largestLucas:
        newLargest = largestLucas + secondLargest
        secondLargest = largestLucas
        largestLucas = newLargest
        lucasList.append(newLargest)
    if n < largestLucas:
        lucasList.pop() #removes last element
    return lucasList

#if ListType == "Fib", gives index of largest Fib number <= n
#if ListType == "Lucas", gives index of largest Lucas number <= n
def maxIndex(n, ListType):
    if ListType == "Fib":
        validList = listSmallFibs(n)
        index = len(validList) + 1
        return index

    elif ListType == "Lucas":
        validList = listSmallLucas(n)
        index = len(validList) - 1
        return index
    #cases give different formula since Fib list starts from F_2,
    #while Lucas list starts from F_0
    else:
        return None

def largestFib(n): #returns largest Fib Number that is <= n
    listed = listSmallFibs(n)
    length = len(listed)
    return listed[length - 1]

def appendToAll(listOfList, nums): #appends nums to end of each list
    #listOfList is a list of lists
    numLists = len(listOfList)
    for i in range(numLists):
        listOfList[i] = listOfList[i] + nums
    return listOfList

#generates terms from a given recurrence (PLRS)
#first list gives initial terms
#second list gives coefficients of recurrence
#limit is number of terms to output
#if PLRS has depth L then need to input first L terms, for coeff
#put the coefficients in backwards starting with c_L
def generateExpansion(initial, coeff, limit):
    numInitial = len(initial)
    assert(numInitial == len(coeff))
    assert(numInitial < limit)
    expansion = [0]*limit
    for i in range(numInitial):
        expansion[i] = initial[i]
    for i in range(numInitial, limit): #gets rest of terms recursively
        summ = 0
        for j in range(numInitial):
            summ = summ + coeff[j]*expansion[i - numInitial + j]
        expansion[i] = summ


    return expansion #returns list with however many elements are needed


######DATA COLLECTION############  

#the idea is to output what you get when adding lead at the front of each result
#have an input for the largest Fib number we are considering
#will have to be careful once we get to 1,just have it spit out enough 1s
#knownDecompsRolling is a placeholder for a list of lists that will become decomps
#valid is a list of Fib numbers we can choose from, removing them as we pass along
def fibBinsDecompIn(lead, valid, largestAllowed, n, knownDecompsRolling):
    if largestAllowed == 1:
        if knownDecompsRolling == []: #edge case: decomps only with 1
            return [1]*n
        ones = [1]*n
        knownDecompsRolling = appendToAll(knownDecompsRolling, ones)
        return knownDecompsRolling
    else:
        #otherwise make lists with largestAllowed and without


    #be sure to remove the last element of valid and update largestAllowed

        return None

#for data collection purposes we can do greedy algorithm and then list the
    #permutations at the end
#list all ways to split Fibonacci Numbers
def fibBinsDecomp(n):
        

    #recursion can append summands to each, use a branch function
    #then collect all perms using permu model at the end
    valid = listSmallFibs(n)
    validDecomps = fibBinsDecompIn([], valid, largestFib(n), n, [])
    l = []
    for decomp in validDecomps:
        l = l + permutations(decomp) #CAREFUL WITH LIST/SET LAYERING
    l = set(l)
    return l

#evaluates poly with given powers included, all coeffs 1
def evalPoly(coeffList, guess):
    summ = 0
    for coeff in coeffList:
        summ = summ + (guess**coeff)
    return summ - 1 #we subtract 1 at the end to get our summation equaling 0

#evaluates derivative of poly with given powers included, all coeffs 1
def evalPolyDeriv(coeffList, guess):
    summ = 0
    for coeff in coeffList:
        if coeff >= 1: #derivative of constant term is 0
            summ = summ + coeff * (guess**(coeff - 1))
    return summ

#runs Bisection Method on a polynomial list of coefficients
#k refers to number of terms we want from the expansion
#all coefficients are 0 or 1 in this version, interval is [0, 1]
#listType = Fib for Fib #s, = Lucas for Lucas #s
#m refers to number of times to bisect (try m = 200 for now)
#remove the first l numbers from the selected list to construct the
#appropriate polynomial
#approximation of alpha_l or beta_l
def polyBisection(k, m, listType, l):
    assert(k >= 3)
    listItOut = []
    if listType == "Fib":
        listItOut = listFib(k)
        if l > 0:         
            for i in range(l):
                listItOut.pop(0)
    elif listType == "Lucas":
        listItOut = listLucas(k)
        if l > 0:
            for i in range(l):
                listItOut.pop(0)
    else:
        print("Not valid type")
        return None
    guess = 0.5

    for i in range(m):
        evalAtPoint = evalPoly(listItOut, guess)
        if evalAtPoint < 0:
            k = guess * 2**(i)
            l = 2*k
            guess = (l + 1)/(2**(i + 1)) #move guess to right
        elif evalAtPoint == 0:
            #print(1/(evalPolyDeriv(listItOut, guess) * guess))
            return guess 
        else: #evalAtPoint > 0
            k = guess * 2**i
            l = 2*k
            guess = (l - 1)/(2**(i + 1)) #move guess to left
        #print("guess = ", guess)
    #print(1/(evalPolyDeriv(listItOut, guess) * guess)) #to print 1/(al*r'(al))
    return guess
    #the guessing is tractable since we know the functions we're using
    #are strictly increasing on [0, 1], so there is only one root

    #eval function to evaluate right polynomial


#generalization of polyBisection for lists besides Fib #s and Lucas #s
#runs Bisection Method on a polynomial list of coefficients
#k refers to number of terms we want from the expansion
#all coefficients are 0 or 1 in this version, interval is [0, 1]
#listType = Fib for Fib #s, = Lucas for Lucas #s
#m refers to number of times to bisect (try m = 200 for now)
#remove the first l numbers from the selected list to construct the
#appropriate polynomial
#approximation of eta_l
#to recover Fibonacci use generateExpansion([1, 2], [1, 1], k)
#to recover Lucas use generateExpansion([2, 1], [1, 1], k)
#suspect there is a bug somewhere based on plugging into RootRateGen
#agrees with polyBisection for Fib and Lucas
def polyBisectionGen(k, m, listContents, l):
    numInList = len(listContents)
    dummyList = [0]*(numInList - l)
    assert(l <= numInList)
    #assert(k <= numInList)
    assert(k >= 3)
    guess = 0.5

    #need to remove l elements

    for i in range(0, numInList - l):
        dummyList[i] = listContents[i + l]

    for i in range(m):
        evalAtPoint = evalPoly(dummyList, guess)
        if evalAtPoint < 0:
            k = guess * 2**(i)
            l = 2*k
            guess = (l + 1)/(2**(i + 1)) #move guess to right
        elif evalAtPoint == 0:
            return guess 
        else: #evalAtPoint > 0
            k = guess * 2**i
            l = 2*k
            guess = (l - 1)/(2**(i + 1)) #move guess to left

    return guess
    #the guessing is tractable since we know the functions we're using
    #are strictly increasing on [0, 1], so there is only one root

    #eval function to evaluate right polynomial

#calculates r^m(n) if listType is "Fib"
#calculates s^m(n) if listType is "Lucas"
def countCompositionsNoHead(m, n, listType):

    if n < 0: return 0
    elif n == 0: return 1
    
    #Case 1: Fibonacci
    if listType == "Fib":
        assert(m >= 2)
        firstFibs = listSmallFibs(n)
        if len(firstFibs) >= m - 1:
            smallestAllowed = firstFibs[m - 2]
        else:
            return 0

        if n < smallestAllowed:
            return 0
        elif n == smallestAllowed:
            return 1
        else: #where we need to actually use the recursion
            summ = 0
            kn = maxIndex(n, "Fib")
            for i in range(m - 2, kn - 1):
                summ += countCompositionsNoHead(m, n - firstFibs[i], "Fib")
            return summ



    #Case 2: Lucas
    elif listType == "Lucas":
        assert(m >= 0)
        firstLucas = listSmallLucas(n)


        #m = 0 is an edge case since the algorithm is greedy
        #but the 2 comes before the 1, so we modify list accordingly in thoat case
        if m == 0 and n >= 2:
            firstLucas[0] = 1
            firstLucas[1] = 2
        elif m == 1:
            if n == 1: return 1
            if n == 2: return 1

            
        if len(firstLucas) >= m + 1:
            smallestAllowed = firstLucas[m]
        else:
            return 0

        if n < smallestAllowed:
            return 0
        elif n == smallestAllowed:
            return 1
        else: #where we need to actually use the recursion
            summ = 0
            tn = maxIndex(n, "Lucas")
            for i in range(m, tn + 1):
                summ += countCompositionsNoHead(m, n - firstLucas[i], "Lucas")
            return summ
    
    return None
        

#if listType == "Fib", prints quantity
#|1 - al_{m + 1}|/|1 - al_m|^{power} for all 2 <= m <= M
#conjecture linear convergence for Fib with rate phi - 1
def rootRate(listType, M, power = phi):
    if listType == "Fib":
        assert(M >= 3) #quality of life assertion
        for m in range(2, M):
            alphaCurr = polyBisection(1000, 200, "Fib", m - 2)
            #print(alphaCurr)
            alphaNext = polyBisection(1000, 200, "Fib", m - 1)
            #print(alphaNext)
            numerator = abs(1 - alphaNext)
            denominator = abs(1 - alphaCurr)**(power)
            print(numerator/denominator)
    elif listType == "Lucas":
        assert(M >= 3) #quality of life assertion
        for m in range(2, M):
            betaCurr = polyBisection(1000, 200, "Lucas", m)
            betaNext = polyBisection(1000, 200, "Lucas", m + 1)
            numerator = abs(1 - betaNext)
            denominator = abs(1 - betaCurr)**(power)
            print(numerator/denominator)

    else:
        return None

#to recover Fibonacci use generateExpansion([1, 2], [1, 1], k)
#to recover Lucas use generateExpansion([2, 1], [1, 1], k)
def rootRateGen(listing, M, power = phi):
    assert(M >= 3)
    for m in range(2, M):
        etaCurr = polyBisectionGen(1000, 200, listing, m - 2)
        print(etaCurr)
        etaNext = polyBisectionGen(1000, 200, listing, m - 1)
        print(etaNext)
        numerator = abs(1 - etaNext)
        denominator = abs(1 - etaCurr) ** power
        #print(denominator)
        print(numerator/denominator)
    return None


#if listType == "Fib" prints alpha_m^m for 2 <= m <= M
#if listType == "Lucas" prints beta_m^m for 0 <= m <= M
def etaPower(listType, M):
    if listType == "Fib":
        assert(M >= 2)
        fibs = listFib(M) #lists fib #s up to the Mth one starting 1, 2, 3, 5, ...
        for m in range(2, M + 1):
            base = polyBisection(1000, 150, "Fib", m - 2)
            print(base**fibs[m - 2])
    elif listType == "Lucas":
        assert(M >= 0)
        lucases = listLucas(M) #lists lcuas #s 2, 1, 3, 4, 7, ...
        for m in range(0, M + 1):
            base= polyBisection(1000, 150, "Lucas", m)
            print(base**lucases[m])

    return None


#to recover Fibonacci use generateExpansion([1, 2], [1, 1], M)
#to recover Lucas use generateExpansion([2, 1], [1, 1], M)
def etaPowerGen(listing, M):
    assert(M == len(listing))
    for m in range(0, M + 1):
        base = polyBisectionGen(1000, 150, listing, m)
        print(base**listing[m])
    return None

#Fibonacci data various algebraic expressions
#auxNum = 1: print
#[1/al^{F_m - 1}_m - al^{1 - F_{m - 1}}_{m + 1}]/
#[1 + al^{F_m - 1}_m - al^{1 - F_{m - 1}}_m + al^{F_{m - 2}}_m]
#which isn't particularly useful

#auxNum = 2: print [al^{F_{m - 1}}_{m + 1} + al^{2F_{m - 1}}_{m + 1} +
#al^{F_{m + 1}}_{m + 1} - al_{m + 1}]/
#1 - al^{F_{m - 1}}_{m + 1}

#auxNum = 3: print al_m/al_{m + 1}

#auxNum = 4: print (1 - al_{m + 1})/(1 - al_m)

#auxNum = 5: print (2 - al_{m + 1} - al_m)/(1 - al_m)

#auxNum = 6: print (3 - al_{m + 1} - 2al_m)/(2 - al_{m+ 1} - al_m)
def auxFib(m, auxNum):
    if auxNum == 1:
        assert(m >= 4)
        thisAl = polyBisection(1000, 200, "Fib", m - 2)#al_m
        nextAl = polyBisection(1000, 200, "Fib", m - 1)#al_{m + 1}
        allRelevantFibs = listFib(m)
        lastFib = allRelevantFibs[m - 2] #F_{m - 1}
        nTLFib = allRelevantFibs[m - 3] #F_{m - 2}, NTL == "next-to-last"
        numerator = 1/(thisAl**lastFib) - nextAl**(1 - lastFib)
        denominator = 1 + thisAl**(lastFib) - thisAl**(1 - lastFib) + thisAl**(nTLFib)
        print(numerator/denominator)
    elif auxNum == 2:
        assert(m >= 4)
        thisAl = polyBisection(1000, 200, "Fib", m - 2)#al_m
        nextAl = polyBisection(1000, 200, "Fib", m - 1)#al_{m + 1}
        allRelevantFibs = listFib(m + 1)
        lastFib = allRelevantFibs[m - 2] #F_{m - 1}
        nextFib = allRelevantFibs[m] #F_m
        numerator = nextAl**lastFib + nextAl**(2*lastFib) + nextAl**(nextFib) - nextAl
        denominator = 1 - nextAl**(lastFib)
        print(numerator/denominator)
    elif auxNum == 3:
        assert(m >= 4)
        thisAl = polyBisection(1000, 200, "Fib", m - 2)#al_m
        nextAl = polyBisection(1000, 200, "Fib", m - 1)#al_{m + 1}
        print(thisAl/nextAl)
    elif auxNum == 4:
        assert(m >= 4)
        thisAl = polyBisection(1000, 200, "Fib", m - 2)#al_m
        nextAl = polyBisection(1000, 200, "Fib", m - 1)#al_{m + 1}
        print((1 - nextAl)/(1 - thisAl))
    elif auxNum == 5:
        assert(m >= 4)
        thisAl = polyBisection(1000, 200, "Fib", m - 2)#al_m
        nextAl = polyBisection(1000, 200, "Fib", m - 1)#al_{m + 1}
        print((2 - nextAl - thisAl)/(1 - thisAl))
    elif auxNum == 6:
        assert(m >= 4)
        thisAl = polyBisection(1000, 200, "Fib", m - 2)#al_m
        nextAl = polyBisection(1000, 200, "Fib", m - 1)#al_{m + 1}
        print((3 - nextAl - 2*thisAl)/(2 - nextAl - thisAl))
    return None

#to recover Fibonacci use generateExpansion([1, 2], [1, 1], M)
#to recover Lucas use generateExpansion([2, 1], [1, 1], M)
#auxNum = 1: print (1 - eta_m)/(1 - eta_{m + 1})
def auxArbSeq(listing, m, auxNum):
    thisEta = polyBisectionGen(1000, 200, listing, m - 2)
    nextEta = polyBisectionGen(1000, 200, listing, m - 1)
    if auxNum == 1:
        numerator = 1 - thisEta
        denominator = 1 - nextEta
        print(numerator/denominator)
    return None

####################################################
############FULL COMPOSITION ROOT APPROXIMATION#####

#guess ga_m as root of t_m(x) = -1 + \sum^{M}_{i = m}x^i in (0, 1), m >= 1
#let k be number of bisection iterations
#notice that equation becomes x^m + x - 1 = 0
def rootFullLocate(m, k):
    guess = 0.5 #initial guess
    for i in range(k):
        evalAtPoint = guess**m + guess - 1
        if evalAtPoint < 0:
            j = guess * 2**(i)
            l = 2*j
            guess = (l + 1)/(2**(i + 1)) #move guess to right
        elif evalAtPoint == 0:
            return guess 
        else: #evalAtPoint > 0
            j = guess * 2**i
            l = 2*j
            guess = (l - 1)/(2**(i + 1))

    return guess

######################################
#####COMPARING al_m to ga_m ###########

#approximates al_m/ga_m where k is number of bisection iterations
def quotAlGa(m, k):
    ga_m = rootFullLocate(m, k)
    al_m = polyBisection(m + 1000, k, "Fib", m) 
    return al_m/ga_m

#approximates al_m/ga_{F_m} where k is number of bisection iterations
def quotAlFibGa(m, k):
    assert(m >= 3)
    mthFib = kthFib(m)
    ga_F_m = rootFullLocate(mthFib, k)
    al_m = polyBisection(m + 1000, k, "Fib", m)
    return al_m/ga_F_m

#############################################################
######COMPARING al_m to (ga_P)_m for specific polynomials P##

##let's compare for P_m = m^8?? Use vector notation and polyeval
#approximates al_m/(ga_P)_m where k is number of bisection iterations
#default for my simulations has been k = 200
def quotAlPolyGa(m, k, poly):
    #input as list where first index is constant term, second is linear, etc
    assert(m >= 3)
    polym = 0
    numCoeff = len(poly)
    for i in range(numCoeff):
        polym = polym + poly[i] * (m**i)
    #print(polym)
    #so now we have P(m)
    ga_P_m = rootFullLocate(polym, k)
    al_m = polyBisection(m + 1000, k, "Fib", m)
    print("al_m = ", al_m, ", ga_P_m = ", ga_P_m)
    return al_m/ga_P_m

###########################
############TEST CASES#####

def runTest():
    assert(listLucas(2) == [2, 1, 3])
    assert(listLucas(4) == [2, 1, 3, 4, 7])
    assert(listLucas(5) == [2, 1, 3, 4, 7, 11])

    assert(listFib(3) == [1, 2, 3])
    assert(listFib(4) == [1, 2, 3, 5])
    assert(listFib(7) == [1, 2, 3, 5, 8, 13, 21])
    
    assert(listSmallFibs(1) == [1])
    assert(listSmallFibs(10) == [1, 2, 3, 5, 8])
    assert(listSmallFibs(13) == [1, 2, 3, 5, 8, 13])

    assert(listSmallLucas(2) == [2, 1])
    assert(listSmallLucas(3) == [2, 1, 3])
    assert(listSmallLucas(11) == [2, 1, 3, 4, 7, 11])
    assert(listSmallLucas(15) == [2, 1, 3, 4, 7, 11])
    assert(listSmallLucas(17) == [2, 1, 3, 4, 7, 11])

    assert(maxIndex(4, "Fib") == 4)
    assert(maxIndex(5, "Fib") == 5)
    assert(maxIndex(13, "Fib") == 7)
    assert(maxIndex(15, "Fib") == 7)
    assert(maxIndex(4, "Lucas") == 3)
    assert(maxIndex(8, "Lucas") == 4)
    assert(maxIndex(11, "Lucas") == 5)
    assert(maxIndex(17, "Lucas") == 5)

    assert(largestFib(1) == 1)
    assert(largestFib(3) == 3)
    assert(largestFib(7) == 5)
    assert(largestFib(34) == 34)
    assert(largestFib(35) == 34)

    assert(countCompositionsNoHead(2,5,"Fib") == 14)
    assert(countCompositionsNoHead(2,6,"Fib") == 26) #these two cases in [Kno]
    assert(countCompositionsNoHead(3, 5, "Fib") == 3)
    assert(countCompositionsNoHead(5, 5, "Fib") == 1)
    assert(countCompositionsNoHead(3, 6, "Fib") == 2)
    assert(countCompositionsNoHead(9, 12, "Fib") == 0)
    assert(countCompositionsNoHead(6, 24, "Fib") == 1)

    assert(countCompositionsNoHead(0, 3, "Lucas") == 4)
    assert(countCompositionsNoHead(0, 4, "Lucas") == 8)
    assert(countCompositionsNoHead(0, 5, "Lucas") == 15)
    assert(countCompositionsNoHead(1, 3, "Lucas") == 2)
    assert(countCompositionsNoHead(1, 4, "Lucas") == 4)
    assert(countCompositionsNoHead(1, 5, "Lucas") == 6)
    assert(countCompositionsNoHead(2, 7, "Lucas") == 3)
    assert(countCompositionsNoHead(2, 9, "Lucas") == 1)
    assert(countCompositionsNoHead(5, 20, "Lucas") == 0)
    assert(countCompositionsNoHead(5, 21, "Lucas") == 0)
    assert(countCompositionsNoHead(5, 22, "Lucas") == 1) #22 = 11 + 11

    assert(generateExpansion([1, 2], [1, 1], 10) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    assert(generateExpansion([2, 1], [1, 1], 10) == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76])
    assert(generateExpansion([3, 1], [1, 1], 10) == [3, 1, 4, 5, 9, 14, 23, 37, 60, 97])
    assert(generateExpansion([1, 1, 1], [1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        
    assert(appendToAll([[1, 2], [1, 2]], [1]) == [[1, 2, 1], [1, 2, 1]])
    print("BAZING!")
    return None
