import itertools

def simple(a):
    if(a > 2):
        if(a % 2 == 1):
            for i in range(3, a+1):
                if(a % i == 0 and a != i):
                    return False
            return True
        else:
            return False
    else:
        return True
    return False

def primes():
    a = 1
    while True:  # просто пример
        a += 1
        if(simple(a)):
            yield a

#print(list(itertools.takewhile(lambda x : x <= 31, primes())))

z = [i + 1 for i in range(4)]
x = [i for i in range(4)]
c = [i for i in range(5)][1:]
v = list(i + 1 for i in range(4))

print(z)
print(x)
print(c)
print(v)