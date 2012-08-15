from itertools import combinations
from lib import primes_to_n
from time import time

L = 15
P = 2**L
K = 2

def count_bits(n):
    c = 0
    while n:
        n &= (n - 1)
        c += 1
    return c

def bias(func, primes):
    s = (N >> K) * count_bits(func)
    t = len([0 for prime in primes if (func & (1 << prime))])
    # t = sum([not not(func & (1 << prime)) for prime in primes])
    return t - s

if __name__ == "__main__":
    #rand_strings = [''.join(random.choice('01') for j in range(L)) for i in range(N)]
    assert(count_bits(11) == 3)
    assert(count_bits(127) == 7)

    print 'P: %d' % P
    print 'K: %d' % K

    start = time()
    
    primes = [x/2 % (P/4) for x in primes_to_n(P) if x > P/2]
    
    N = len(primes)

    best = 0
    for comb in combinations(range(L - 2), K):
        for func in xrange(1 << K):
            # the second thing makes a list of numbers from the bits given in comb
            b = bias(func, [sum([2**i for i in range(len(comb)) if prime & (1 << comb[i])]) for prime in primes])
            if b > best - 3:
                print "bias of function %d on bits %s: %d" % (func, comb, b)
                if b > best:
                    best = b
    
    print time() - start
