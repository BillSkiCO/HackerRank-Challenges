#!/bin/python3

# https://www.hackerrank.com/challenges/30-queues-stacks

# Implementing queues and stacks using lists in python

import sys

# Begin code
# Use list as Stack (LIFO)
stk = []

# Use list as Queue (FIFO)
que = []

class Solution:
    def __init__(self):
        pass
    
    def pushCharacter(self, char):
        stk.append(char)
        
    def enqueueCharacter(self, char):
        que.append(char)
        
    def popCharacter(self):
        return stk.pop()
    
    def dequeueCharacter(self):
        return que.pop(0)
# End Code

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
