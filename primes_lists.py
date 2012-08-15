from math import log
from itertools import combinations
from lib import primes_to_n, memoized
from time import time

P = 32768
K = 3

def pad(nums, m):
    return [x + [0] * (m - len(x)) for x in nums]

def generate_funcs():
    return pad(map(num2bin, range(2**(2**K))), 2**K)
    
def get_funcs2():
    return range(2**K)

def bin2num(string):
    r = 0
    for i in reversed(string):
        r = r << 1
        r += i
    return r

def num2bin(n):
    if n == 0: return [0]
    return [(n/(2**i)) % 2 for i in range(int(log(n, 2)) + 1)]

def apply(func, string):
    return func[bin2num(string)]

def bias(func, strings):
    s = (N/(2**K)) * sum(func)
    t = sum([func[bin2num(string)] for string in strings])
    return t - s

if __name__ == "__main__":
    #rand_strings = [''.join(random.choice('01') for j in range(L)) for i in range(N)]
    assert(bin2num([1,1,0]) == 3)
    assert(num2bin(3) == [1,1])
    assert(pad([[1], [1,1]], 3) == [[1,0,0], [1,1,0]])

    start = time()
    
    primes = [x/2 % (P/4) for x in primes_to_n(P) if x > P/2]
    
    L = int(log(primes[-1], 2)) + 1
    
    N = len(primes)
    
    prime_strings = pad(map(lambda x: num2bin(x), primes), L)
    
    best = 0
    funcs = generate_funcs()
    for i in combinations(range(L), K):
        for func in funcs:
            b = bias(func, [map(lambda x: string[x], i) for string in prime_strings])
            if b > best - 3:
                print "bias of function " + str(func) + " on bits " + str(i) + ": ", b
                if b > best:
                    best = b
    print time()-start