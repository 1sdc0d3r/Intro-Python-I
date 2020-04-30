num = input("Enter a number greater than 1: ")
num = int(num)


def SieveOfEratosthenes(num):
    prime = [True for n in range(num + 1)]
    p = 2
    while(p * p <= num):
        if(bool(prime[p])):
            for i in range(p*p, num+1, p):
                prime[i] = False
        p += 1
        for p in range(2, num):
            if (prime[p]):
                print(p)


SieveOfEratosthenes(num)
