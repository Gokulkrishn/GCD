## returns list of all primes
def Primes(num):
    for i in range(2,num):
        if (num%i == 0):
            return False
    else:
        return True
