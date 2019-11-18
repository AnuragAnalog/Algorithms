#!/usr/bin/python3

import os

def input_data(n: int) -> list:
    arr = list()
    for i in range(n):
        arr.append(int(input("Enter value: ")))

    return arr

def find_optimum_cost(weight: list, prices: list, n: int):
    grid = [[0 for i in range(n)] for j in range(n)]

    for i in range(n-1, 0, -1) :
        for j in range(n-i) :
            grid[i][j] =  
if __name__ == '__main__':
    n = int(input("Enter the no of items: "))

    print("Enter the weights of each element: ")
    weight = input_data(n)
    print("Enter the prices of each element: ")
    prices = input_data(n)
