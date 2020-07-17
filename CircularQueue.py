# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:54:21 2020

@author: COPPERHEAD
"""


class CircularQueue:
    
    class _Node:
        __slots__='_element','_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
       
    def __init__(self):
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        if(not self.is_empty()):
            old_head = self._tail._next
            if(self._size == 1):
                self._tail = None
            else:                
                self._tail._next = old_head._next
            self._size -= 1
            return old_head._element
                
    def enqueue(self,n):
        newNode = self._Node(n, None)
        if(self.is_empty()):
            newNode._next = newNode
        else:
            newNode._next = self._tail._next 
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1
        
    def first(self):
        if(not self.is_empty()):
            return self._tail._next._element
            
if __name__ == '__main__':
    cq = CircularQueue()
    for i in range(10):
        cq.enqueue(i)

    print(cq.first())        
    cq.dequeue()
    print(cq.first())        
    cq.dequeue()
    print(cq.first())        
    cq.dequeue()                
    print(cq.first())           