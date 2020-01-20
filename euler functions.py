import math

def lowestfactor(n):    #find lowest prime factor of a number or return the number itself (if number is prime)
    if n == 2: return n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            found = 1
            for j in range(1, i):
                if i % j == 0 and j != 1:
                    found = 0
                    break            
            if found:
                factor = (i)
                return factor
    return n

def primefactors(number):   #find all the prime factors of a number
    primes = []
    nonprimes = []
    nonprimes.append(number // lowestfactor(number))
    primes.append(lowestfactor(number))
    while True:
        x = nonprimes.pop()
        primes.append(lowestfactor(x))
        if x == lowestfactor(x): break
        nonprimes.append(x // lowestfactor(x))
    return primes

def rprimefactors(n):   #revursively find all primefactors of a number
    #find lowest factor of n
    pfactors = [lowestfactor(n)]
    #divide n by its lowest factor, then proceed to find the lowest factors of that
    other = n // pfactors[0]
    if other == 1:
        return pfactors
    else:
        pfactors.extend(rprimefactors(other))
        return pfactors

def findprimes(start, stop):    #erasthones sieve for finding primes in a given range (from start to stop)
    if start == 1:
        numbers = [2] + list(range(3, stop, 2))
    elif start % 2 == 0:
        numbers = list(range(start + 1, stop + 1, 2))
    elif start % 2 != 0 :
        numbers = list(range(start, stop, 2))
    p = 2
    while p ** 2 <= max(numbers):
        for i in numbers:
            if (i == p**2 or i % p == 0) and p != i:
                numbers.remove(i)
        p +=1
        if not numbers: break
    return numbers
    
def findprimesblock(start, stop, block):    #repeats findprimes function in a given block, mainly so user can see progress when finding a very large amount of primes
    count = 0
    primes = []
    a = start; b = a + block
    while True:
        primes.extend(findprimes(a, b))
        if max(primes) > stop:
            break
        else:
            a = b; b = a + block; count += 1
            print('{}/{}'.format(count, stop // block))
    return primes
