#! /bin/python3
"""
Given two strings (a) and (b) determine if they share a common substring.

Input Format:

The first line contains a single integer, p , denoting the number of pairs you must check.
Each pair is defined over two lines:

    The first line contains string (a).
    The second line contains string (b).

Constraints:

(a) and (b) consist of lowercase English letters only.
1 <= p <= 10
1 <= |a|,|b| <= 10^5

Output Format:

For each (a,b) pair of strings, print YES on a new line if the two strings share a common substring;
if no such common substring exists, print NO on a new line.

Sample Input:
2
hello
world
hi
world

Sample Output:
YES
NO
"""
__author__ = "William Golembieski"
__email__ = "BillGolembieski@projectu23.com"

n = int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

for j in range(0, n*2, 2):
    # & returns only the intersection of the 2 sets
    x = set(string_list[j]) & set(string_list[j+1])
    if len(x) > 0:
        print('YES')
    else:
        print('NO')
