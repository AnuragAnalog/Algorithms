#!/usr/bin/python3

"""

    Knapsack Problem: Given a set of items with their weights and price 
associated with them and a knapsack with a capacity, find the collection of 
items with weights less than the capacity and the Total price as large as
possible.

"""

import sys
import numpy as np

class Knapsack():
    def input_data(self, n: int) -> (np.array, np.array, np.array):
        """
            Takes a argument n(no. of items) and returns a tuple of
        three numpy arrays (price, weight, quantity) of the items.

        Note: This is only useful when you this whole file as a
        program.
        """
        p = list()
        w = list()
        q = list()
        for i in range(n):
            p.append(float(input("Enter the price of item {}: ".format(i+1))))
            w.append(float(input("Enter the weight of item {}: ".format(i+1))))
            q.append(float(input("Enter the quantity of item {}: ".format(i+1))))
            print("")
        return np.array(p), np.array(w), np.array(q)

    def fractional(self, p: np.array, w: np.array, q: np.array, c: int) -> (int, np.array):
        """
            Knapsack problem which assumes that the object can be divided into
        pieces and can be put into.

        p: Prices of the items
        w: Weights of the items
        q: Qunatity of the items
        c: Capacity of knapsack

        Return: A tuple of Total-profit and list of Qunatity selected.
        """
        if len(p) != len(w):
            print("Dimension Mismatch")
            sys.exit()

        pbyw = p/w

        sack = [0 for i in range(len(p))]
        profit = 0
        for val in sorted(zip(pbyw, p, w, range(len(p)), q), reverse=True):
            if c == 0:
                break

            prof = val[1]*val[4]
            weig = val[2]*val[4]
            if weig <= c:
                c = c - weig
                profit = profit + prof
                sack[val[3]] = val[4]
            elif val[2] > c:
                profit = profit + (c/val[2])*val[1]
                sack[val[3]] = c/val[2]
                c = 0
        return profit, sack

    def zerone(self, p: np.array, w: np.array, q: np.array, c: int) -> (int, np.array):
        """
            Knapsack problem which assumes that the object cannot be divided 
        into pieces either included or not.

        p: Prices of the items
        w: Weights of the items
        q: Qunatity of the items
        c: Capacity of knapsack

        Return: A tuple of Total-profit and list of Qunatity selected.
        """
        if len(p) != len(w):
            print("Dimension Mismatch")
            sys.exit()

        pbyw = p/w

        sack = [0 for i in range(len(p))]
        profit = 0
        for val in sorted(zip(pbyw, p, w, range(len(p)), q), reverse=True):
            if c == 0:
                break

            prof = val[1]*val[4]
            weig = val[2]*val[4]
            if weig <= c:
                c = c - weig
                profit = profit + prof
                sack[val[3]] = val[4]
        return profit, sack

if __name__ == '__main__':
    # This section is only for testing purpose.
    k = Knapsack()

    n = int(input("Enter the no of items: "))
    c = float(input("Enter the capacity of the knapsack: "))

    x, y, z = k.input_data(n)
    print(k.fractional(x, y, z, c))
    print(k.zerone(x, y, z, c))
