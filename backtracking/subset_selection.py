#!/usr/bin/python3

def input_data(n: int) -> list:
    arr = list()

    for i in range(n):
        arr.append(int(input("Enter the value: ")))
    return arr

def subset(array: list, value: int) -> bool:
    arr_sum = 0
    for element in array:
        tmp = array.copy()
        tmp.remove(element)

        status = findsubset(tmp, arr_sum + element, value)
        if status:
            return True
    return False

def findsubset(rem_arr: list, arr_sum: int, value: int) -> bool:
    if arr_sum > value:
        return False
    elif arr_sum == value:
        return True
    else:
        for element in rem_arr:
            tmp = rem_arr.copy()
            tmp.remove(element)

            status = findsubset(tmp, arr_sum + element, value)
            if status:
                return True

if __name__ == '__main__':
    n = int(input("Enter the no of elements: "))
    array = input_data(n)

    value = int(input("Enter the Value: "))
    stat = subset(array, value)

    if stat:
        print("Subset Possible")
    else:
        print("Subset Not Possible")
