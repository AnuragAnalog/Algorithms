#!/usr/bin/python3

from itertools import combinations

def input_data(n: int) -> list:
    arr = list()
    for i in range(n):
        arr.append(int(input("Enter value: ")))

    return arr

def print_set(arr: set) -> None:
    for e in arr:
        print(e, end=" ")
    print()

    return

def find_gcd(some_list: list) -> int:
    gcd = 1
    num = min(some_list)
    for i in range(1, num+1):
        no = 0
        for j in range(len(some_list)):
            if some_list[j]%i == 0:
                no = no + 1
        if no == len(some_list):
            gcd = i
    return gcd

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))

    arr = input_data(n)
    gcds = set()
    for i in range(1, n+1):
        permut = combinations(arr, i)
        for p in permut:
            gcds.add(find_gcd(p))
    print("Distinct GCD's:", len(gcds))
    print_set(gcds)
