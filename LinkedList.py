#!/bin/python3

# https://www.hackerrank.com/challenges/30-linked-list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next            

# Begin Code   
    def insert(self,head,data): 
        # Create new node from Node Class with data
        new_node = Node(data)
        
        # Check if this is the head node
        if(head == None):
            return new_node
        
        # Step through linked list starting at head until end
        current = head
        while current:
            if(current.next == None):
                current.next = new_node
                return head
            else:
                current = current.next
# End Code

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
