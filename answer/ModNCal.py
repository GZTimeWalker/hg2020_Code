from random import randint

def quickMulMod(a, b, m):
    '''a*b%m,  quick'''
    ret = 0
    while b:
        if b & 1:
            ret = (a + ret) % m
        b//=2
        a = (a + a) % m
    return ret

def quickPowMod(a, b, m):
    '''a^b %m, quick,  O(logn)'''
    ret = 1
    while b:
        if b & 1:
            ret = quickMulMod(ret, a, m)
        b//=2
        a = quickMulMod(a, a, m)
    return ret

def isPrime(n, t = 5):
    '''miller rabin primality test,  a probability result
        t is the number of iteration(witness)
    '''
    t = min(n-3, t)
    if n < 2:
        print('[Error]: {} can\'t be classed with prime or composite'.format(n))
        return
    if n==2: return True
    d = n-1
    r = 0
    while d%2==0:
        r+=1
        d//=2
    tested=set()
    for i in range(t):
        a = randint(2,n-2)
        while a in tested:
            a = randint(2,n-2)
        tested.add(a)
        x= quickPowMod(a,d,n)
        if x==1 or x==n-1: continue  #success,
        for j in range(r-1):
            x= quickMulMod(x,x,n)
            if x==n-1:break
        else:
            return False
    return True

def gcd(a,b):
    return a if b == 0 else gcd(b, a % b)

def exgcd(a,b):
	if b == 0:
		return 1, 0
	else:
		k = a // b
		remainder = a % b
		x1, y1 = exgcd(b, remainder)
		x, y = y1, x1 - k * y1
	return x, y

