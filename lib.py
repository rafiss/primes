import itertools

def erat():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p
            
def nth_prime(n):
    return list(itertools.islice(erat(),n-1,n))[0]
    
def first_n_primes(n):
    return list(itertools.islice(erat(),0,n))

def primes_to_n(n):
    e = erat()
    a = []
    t = e.next()
    while t<=n:
        a.append(t)
        t = e.next()
    return a
