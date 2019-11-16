# Brute-Froce search

A Bruteforce search is an exhaustive search where we list out all the possible candidates and test whether the condition is satisfied for each of the generated candidate.

It gives a solution if there exists one.

For most of the real-world problems, we don't use this method because as the size grows, the test which we have to generate increases drastically (combinatorial explosion).

It is easy to implement.

This method is advisable when the problem size is small.

## Problems

**Binary String n**

List all the binary string from length 1 to n

| Time Complexity | Space Complexity |
| --- | --- |
| O(2^n) | O(2^n) |

**Subset GCD**

Given a list of numbers, find gcd of all the possible subsets of the list.

| Time Complexity | Space Complexity |
| --- | --- |
| O(2^n) | O(2^n) |
