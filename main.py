import itertools

def main(n):
    cubes = []
    expandedCubes = []
    primeNumbers = generatePrimes(n)
    product = 1
    for i in primeNumbers:
        product = product * i**2

    generateCubes(primeNumbers, cubes)
    removeNot4(cubes, primeNumbers, expandedCubes, n)
    print('expanded cubes =', len(expandedCubes))
    print('not rotated cubes =', len(removeIso(expandedCubes)))
    print(removeIso(expandedCubes))
    count = 0
    number = 0
    for i in itertools.combinations(removeIso(expandedCubes), n):
        if len(findSAM(solveMatrix(i, n, product), n)) > 0:
            number += 1
    print('----')
    print('total =', count)
    print('solvable =', number)

def checkPrime(number):
    for a in range(2, int(number**.5)+1):
        if number%a==0:
            return False
    return True

def generatePrimes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if checkPrime(i)==True:
            primes.append(i)
        i+=1
    return primes

def findPrimeFactors(n, primeNumbers):
    for i in primeNumbers:
        for k in primeNumbers:
            if n == i * k:
                return (i, k)


def generateCubes(primeNumbers, cubes):
    for c1,c2,c3,c4,c5,c6 in itertools.product(primeNumbers, repeat=6):
        cubes.append([c1 * c5, c2 * c4, c3 * c6])


def removeNot4(cubes, primeNumbers, expandedCubes, n):
    for i in cubes:
        setCheck = set()
        for j in range(3):
            for k in range(2):
                setCheck.add(findPrimeFactors(i[j], primeNumbers)[k])
        if len(setCheck) == n:
            expandedCubes.append(i)


def rotate(a, b, c, set):
    set2 = set.copy()
    set2[0] = set[a]
    set2[1] = set[b]
    set2[2] = set[c]
    return set2


def checkRotate(s1, s2):
    #check if the matrix can be rotated
    for a,b,c in itertools.permutations([0,1,2],3):
        if rotate(a,b,c,s2)==s1:
            return True
    return False

def removeIso(the_list):
    final_list = []
    for m in the_list:
        if final_list == []:
            final_list.append(m)
        else:
            if not any(checkRotate(m, l) for l in final_list):
                final_list.append(m)
    return final_list
'''
def generateVAM():
    VAMs = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    VAMs.append([(0,i),(1,j),(2,k),(3,l)])
    return VAMs
'''
def generateDynamicVam(depth):
    def doLevel(level):
        if (level == 0):
            return [[x] for x in range(3)]
        elif level > 0:
            currentList = doLevel(level - 1)
            newList = []
            for t in currentList:
                for i in range(3):
                    newList.append([*t, i])
            return newList

    def tupelize(listOfLists):
        result = []
        for list in listOfLists:
            newlist = []
            for i in range(len(list)):
                newlist.append((i, list[i]))
            result.append(newlist)
        return result


    return tupelize(doLevel(depth))

def solveMatrix(matrix, n, product):
    solutions = []
    for i in generateDynamicVam(n-1):
        newProduct = 1
        for j in i:
            newProduct = newProduct * matrix[j[0]][j[1]]
        if newProduct==product:
            solutions.append(i)
    return solutions

def findSAM(VAM, n):
    solutions = []
    for i,j in itertools.combinations(VAM, 2):
        tupleSet = set()
        for k in i:
            tupleSet.add(k)
        for l in j:
            tupleSet.add(l)
        if len(tupleSet)==2*n:
            solutions.append([i,j])
    return solutions


#main(int(input('How many cubes in a tower?')))
#print(findSAM(solveMatrix([[21,35,6],[35,9,10],[10,14,21],[6,4,35]], 4, 44100),4))
print(generateDynamicVam(2))