def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def binomial(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))

def b(x,n,p):
    return binomial(n,x)* p**x * (1-p)**(n-x)
 
def binomial_distribution(prob,n):
    p = prob /100
    morethan = 0
    for i in range(0,3):
        morethan += b(i,n,p)
        i +=1
    print(round(morethan,3))
    atleast = 0
    for i in range(2,n):
        atleast += b(i,n,p)
        i +=1
    print(round(atleast,3))

p,n=map(int,input().split())
binomial_distribution(p,n)
