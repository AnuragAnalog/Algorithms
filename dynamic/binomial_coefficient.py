#!/usr/bin/python3

def c(n: int, k: int) -> int:
    arr = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(i+1):
            if j in [0, i+1]:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    return arr[n][k], arr

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    k = int(input("Enter the value of k: "))

    val = c(n, k)
    print(str(n)+"C"+str(k)+" is "+str(val))
