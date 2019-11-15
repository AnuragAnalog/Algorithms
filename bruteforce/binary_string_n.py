#!/usr/bin/python3

"""
    Power set generation using binary numbers(strings)
"""

def binary_str(n):
    strings = ["0","1"]

    for i in range(2, n+1):
        tstr = list()
        low = len(strings) - (2**(i-1))
        tmp = strings[low:]
        for j in range(int((2**i)/2)):
            tstr.append("0"+tmp[j])
            tstr.append("1"+tmp[j])
        strings.extend(tstr)

    return strings

if __name__ == '__main__':
    n = int(input("Enter the value: "))

    bin_str = binary_str(n)
    print(bin_str)
