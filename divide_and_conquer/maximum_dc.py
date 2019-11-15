#!/usr/bin/python3

"""
    Find the maximum in the array using divide and conquer rule.
"""

def input_data(n: int) -> list:
    arr = list()

    for i in range(n):
        arr.append(float(input("Enter element no.{}: ".format(i+1))))

    return arr

def maximum(arr: list, low: int, high: int) -> int:
    if low == high:
        return arr[low]

    mid = int((low+high)/2)
    maxl = maximum(arr, low, mid)
    maxr = maximum(arr, mid+1, high)

    return max(maxl, maxr)

if __name__ == '__main__':
    n = int(input("Enter no. of elements in array: "))

    start = 0

    arr = input_data(n)
    maxi = maximum(arr, start, len(arr)-1)

    print("Maximum element in the array is:", maxi)
