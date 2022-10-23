

#given the coefficients of a PLRS, find the first numTerms terms in recurrence
def computePLRSTerms(coeffs, numTerms):
    depth = len(coeffs)
    assert(coeffs[depth - 1] > 0) #necessary to have a PLRS
    assert(depth >= 1)
    assert(depth <= numTerms)
    expansion = [1] #first term of PLRS is always 1
    for i in range(1, len(coeffs)): #to determine remaining initial terms
        nextInitial = 1
        for j in range(i):
            nextInitial = nextInitial + expansion[i - j - 1]*coeffs[j]   #indexing off     
        expansion.append(nextInitial)
    for i in range(depth, numTerms): #won't enter if depth==numTerms
        nextTerm = 0
        for j in range(depth):
            nextTerm = nextTerm + expansion[i - j - 1]*coeffs[j]
        expansion.append(nextTerm)
    return expansion

#compares two PLRSs up to a certain number of terms and indicates which bigger
#focus on when two PLRSs have same depth and different coefficients first
def comparePLRS(coeffs1, coeffs2, numTerms):
    expansion1 = computePLRSTerms(coeffs1, numTerms)
    expansion2 = computePLRSTerms(coeffs2, numTerms)
    for i in range(numTerms):
        if expansion1[i] == expansion2[i]:
            boo = "tie"
        elif expansion1[i] > expansion2[i]:
            boo = "expansion1 faster"
        else:
            boo = "expansion2 faster"
        print(expansion1[i], expansion2[i], boo)
    return None


def runTests():
    assert(computePLRSTerms([1, 2], 2) == [1, 2])
    assert(computePLRSTerms([1, 2], 3) == [1, 2, 4])
    assert(computePLRSTerms([1, 2], 5) == [1, 2, 4, 8, 16])
    assert(computePLRSTerms([2, 3], 2) == [1, 3])
    assert(computePLRSTerms([2, 3], 5) == [1, 3, 9, 27, 81])
    assert(computePLRSTerms([1, 2, 3], 5) == [1, 2, 5, 12, 28])
    assert(computePLRSTerms([1, 2, 3], 7) == [1, 2, 5, 12, 28, 67, 159])
    assert(computePLRSTerms([1, 1, 1, 2], 5) == [1, 2, 4, 8, 16])
    print("BAZING!")


#see FROM FIBONACCI NUMBERS TO CENTRAL LIMIT TYPE THEOREMS for needed
#defnitions or see preprint
