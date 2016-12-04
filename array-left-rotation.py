#!/bin/python3
"""
    **Challenge:**
    A left rotation operation on an array of size (n) shifts each of the array's elements unit to the left. 
    For example,if left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

    Given an array of (n) integers and a number,(d) , perform left rotations on the array. 
    Then print the updated array as a single line of space-separated integers.
    ------------------------------------------------------------
    **Solution notes:**
    Adding and deleting values to the start and end of an array should trigger "lists" in your mind.
    This solution utilizes python's built-in list data type. Method usage in this solution is as follows
    
    list.append(x)
    Add an item to the end of the list. Equivalent to a[len(a):] = [x].

    list.pop([i])

    Remove the item at the given position in the list, and return it. If no index is specified, a.pop()
    removes and returns the last item in the list. 
    (The square brackets around the i in the method signature denote that the parameter is optional,
    not that you should type square brackets at that position.
    You will see this notation frequently in the Python Library Reference.)
    
    For further method documentation see: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

    Initial implementation: December 4, 2016
"""

__author__ = "William Golembieski"
__github__ = "https://github.com/BillSkiCO"

# Store all first line numbers in array
conditions = input().strip().split(' ')

# Store all second line numbers in array
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def left_shift(array, num_left_shifts):
    """ Input: Un-shifted array, number of left shifts to perform
        Output: None. Global array is changed. """
    for step in range(num_left_shifts):
        temp = int(array[0])
        array.append(temp)
        array.pop(0)
    
    
def format_answer(answer_array):
    """ Input: Array with correct index values for solution
        Output: String that is correctly formatted for the challenge."""
    ans_string = ""  
    
    for num in arr:
        ans_string += str(num) + " "
        
    ans_string.strip(" ")
    return ans_string

left_shift(arr, int(conditions[1]))
ans = format_answer(arr)
    
print(ans)