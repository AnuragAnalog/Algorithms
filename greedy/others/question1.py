#!/usr/bin/python3

def input_data(n):
    array = list()
    for i in range(n):
        array.append(int(input("Enter the Value of item {}: ".format(i+1))))
        print("")
    return array

def check_any_non_zero(array):
    for element in array:
        if element > 0:
            return True
    return False

def rob_alternate_item(array, n):
    t_arr = array.copy()

    maxi = 0
    for i in range(n):
        local_maxi = max(t_arr)
        maxi = maxi + local_maxi

        index = t_arr.index(local_maxi)
        if index - 1 in range(0, n):
            t_arr[index-1] = 0
        if index + 1 in range(0, n):
            t_arr[index+1] = 0
        t_arr[index] = 0

        if check_any_non_zero(t_arr) == False:
            break
    return maxi

if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    array = input_data(n)

    maximum = rob_alternate_item(array, n)
    print("The maximum loot is", maximum)
