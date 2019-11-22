## this will return of list of all primes between 2 to specified number

from primes import Primes

def ListOfPrimes(num):
    listofPrimenumbers = []
    for i in range(2,num):
        if Primes(i):
            listofPrimenumbers.append(i)
    return listofPrimenumbers

