#!/usr/bin/python3

def input_data(n: int) -> list:
    arr = list()
    for i in range(n):
        arr.append(int(input("Enter value: ")))

    return arr

def gcd(x: int, y: int) -> int:
   while(y):
       rem = x%y
       x = y
       y = rem

   return x

def gcds_contiguous_seq(arr: list) -> dict:
    gcds = dict()
    grid = [[0 for i in range(len(arr))] for j in range(len(arr))]

    for i in range(len(arr)):
        grid[i][i] = arr[i]

    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            grid[i][j] = gcd(grid[i][j-1], arr[j])
            gcds[tuple(arr[i:j+1])] = grid[i][j]

    return gcds

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))

    arr = input_data(n)
    gcd_seq = gcds_contiguous_seq(arr)
    print(gcd_seq)
