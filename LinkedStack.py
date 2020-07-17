# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:00:16 2020

@author: Gunjan
"""

from SinglyLinkedList import _LinkedList

class LinkedStack:
        
    def __init__(self,sllist):
        self._list = sllist
        self._size = 0
                      
    def push(self, e):
        self._list.insertFirst(e)
       
    def top(self):
        if(not self._list.isEmpty()):
            return self._list.first()._element
        
    def pop(self):
        self._list.remove_first()

class _Stack:
    
    class _Node:
        __slots__='_element','_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._size = 0
        self._top = None
        
    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self,e):
        newNode = self._Node(e,None)
        if(self.is_empty()):
            self._top = newNode
        else:
            newNode._next = self._top
            self._top = newNode
        self._size += 1    

    def top(self):
        if(self.is_empty()):
            return None
        else:
            return self._top._element
        
    def pop(self):       
        if(not self.is_empty()):
           self._top = self._top._next
        self._size -= 1       

    def printList(self):
        temp = self._top
        while(temp is not None):
            print(temp._element)
            temp = temp._next
            
if __name__ == '__main__':
    print("--------Stack Using List class-----------------")
    sllist = _LinkedList()
    ls = LinkedStack(sllist)
    for i in range(1,100,5):
        ls.push(i)
    # ls.push(4)
    print("top="+str(ls.top()))
    ls.pop()
    sllist.printList()
    
    print("--------Stack Using Inbuilt List-----------------")
    s = _Stack()
    for i in range(1,50,5):
        s.push(i)
    # ls.push(4)
    s.printList()        
    print("top="+str(s.top()))
    s.pop()
    s.printList()
    
    print("--------Reverse Data using Stack-----------------")