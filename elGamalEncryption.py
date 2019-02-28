import random
import math

def findPrimitiveRoot(p):
    #getting a random integer from 2 to p-2 which will be a generator element or a primitive root of <Zp*,x>
    #ie. a^k % p =1 for some k. if k is phi(p) then a is a primitive root.
    #Here phi(p) = p-1
    a=random.randint(2,p-1)
    while(pow(a, p-1, p) !=1):
        a=random.randint(2,p-1)
    return a

def findKey(p):
    # 2.Select a random member from the group <Zp*, x> such that d belongs to [1,p-2]
    ans={}
    d=random.randint(1,p-1)
    while(gcd(d,p)!=1):
        d=random.randint(1,p-1)

    # 3.Select primitive root of the group <Zp*, x>
    e1=findPrimitiveRoot(p)
    print(e1)
    #e2= e1^d % p
    e2=pow(e1,d,p)
    print(e2)
    #Public Key: (e1,e2,p)
    #private key: d
    return {'e1' : e1, 'e2': e2, "d" : d}

def elGamalEncryption(plainText,p):
    E=findKey(p)
    # print E
    r=random.randint(1,p)
    while(gcd(r,p)!=1):
        r=random.randint(1,p)
    #c1=e1^r%p
    #c2= (plainText*e2^r)%p
    c1=pow(E["e1"],r,p)
    c2=(plainText*pow(E["e2"],r,p))%p
    print("c1 and c2 are "+str(c1)+", "+str(c2))
    return {'c1' : c1, 'c2': c2 , "d" : E["d"]}

def elGamalDecryption(c1,c2,d,p):
    P=(c2*pow(c1,(p-1)-d,p))%p
    print("Plaintext after decryption is "+str(P))
    # return P
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0 or n%3 == 0:
        return False
    r, d = 0, n - 1
    #ACCORDING TO FERMAT TEST a^(n-1)% n =1 if n is prime.
    #HERE n-1 is an even number.
    #which is to be written as d*2^r
    #finding the value of d and r
    while d % 2 == 0:
        r += 1
        d //= 2
    # i need to do a^(d*2^r) for miller_rabin
    for iterator in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        #if a^d itself is 1 or -1 then i continue with some other value of "a"
        if x == 1 or x == n - 1:
            continue
        for iterator1 in range(r - 1):
            #(((((a^d)^2)^2)^2)^2)..... r times
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

plaintText=int(input("Enter the text you want to encrypt: "))
# 1.Selecting a large Prime p
p=int(input("Enter a large prime: "))
# print("Please enter a larger prime!: ")
# p = int(input("Prime: ")
#prime:
if(plaintText < p):
    while (miller_rabin(p,25) ==  False):
    	p=int(input("Enter valid prime: "))

    C = elGamalEncryption(plaintText,p)
    elGamalDecryption(C["c1"],C["c2"],C["d"],p)
else:
    print("Prime number too small!")
