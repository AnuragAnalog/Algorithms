#!/usr/bin/python3

def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        fac = [1,1]
        for num in range(2, n+1):
            fac.append(num * fac[num-1])

    return fac[n]

if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    n_fac = factorial(n)
    print("{}! is {}".format(n, n_fac))
