#!/bin/python3

# https://www.hackerrank.com/challenges/30-scope

# Note: Thit was the first submission, an alternate O(n) solution would be to
# loop through the array 1 time, grabbing max and min then doing subtraction.
# This solution is O(n * log(n)) runtime and O(n) space complexity

class Difference:
    def __init__(self, a):
        self.__elements = a
        # Begin Code
        self.maximumDifference = None

    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = self.__elements[-1] - self.__elements[0]
        #End Code

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
        
