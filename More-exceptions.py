#!/bin/python3

# https://www.hackerrank.com/challenges/30-more-exceptions

# Making a Calculator class that calculates a**b while (a,b) are Positive
# Raise and exception if a or b are negative

# Begin code
class Calculator:
    def __init__(self):
        pass
    
    def power(self,a,b):
        if(a < 0 or b < 0):
            raise ValueError('n and p should be non-negative')
        else:
            return a**b
# End code
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
