#!/bin/python3
# -*- coding: utf-8 -*-

"""

Given a square matrix of size N x N calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer N. The next N lines denote the matrix's rows, with each line containing
N space-separated integers describing the columns.

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15

Explanation

The primary diagonal is:
11
      5
            -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
            4
      5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
--
I wanted to practice recursion a bit more so that was the solution that I implemented.
100% passing all tests.
--
"""

__author__ = "William Golembieski"

# Size
n = int(input().strip())

# instantiate empty list
a = []

# Populate 2D array as list[list[]]
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

max_index = n-1


def get_primary_diagonal(index_num):
    """
    Pass max index number to start
    """
    # Base case
    if index_num == 0:
        return a[0][0]

    # Walk from bottom right a[max][max] to base case a[0][0]
    else:
        return a[index_num][index_num] + get_primary_diagonal(index_num-1)


def get_secondary_diagonal(x, y):
    """
    Pass max index number for x, 0 for y to start
    """
    # Base case
    if x == 0 and y == max_index:
        return a[0][max_index]

    # Walk from bottom left to top right until base case
    else:
        return a[x][y] + get_secondary_diagonal(x-1, y+1)

primary = get_primary_diagonal(max_index)
secondary = get_secondary_diagonal(max_index,0)

print(abs(primary - secondary))
