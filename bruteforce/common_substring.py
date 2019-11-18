#!/usr/bin/python3

def common_substr(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0, ""

    if len(str1) < len(str2):
        min_len_string = str1
        max_len_string = str2
    else:
        min_len_string = str2
        max_len_string = str1

    maxi_str = ""
    maxi_len = 0

    for i in range(len(min_len_string)):
        for j in range(i, len(min_len_string)):
            if min_len_string[i:j+1] in max_len_string:
                if maxi_len < j-i+1:
                    maxi_len = j-i+1
                    maxi_str = min_len_string[i:j+1]
    return maxi_len, maxi_str

if __name__ == '__main__':
    str1 = input("Enter First String: ")
    str2 = input("Enter Second String: ")

    length, string = common_substr(str1, str2)
    print("Longest Common substring is", string, "of length", length)
