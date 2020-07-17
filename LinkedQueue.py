# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:54:07 2020

@author: Gunjan
"""


from SinglyLinkedList import _LinkedList

class LinkedQueue:
    
    def __init__(self, sllist):
        self._list = sllist
        
    def enqueue(self,e):
        self._list.insertLast(e)    
        
    def dequeue(self):
        self._list.remove_first()

class _Queue:
    
    class _Node:
        __slots__='_element','_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._head = None
        self._size = 0
        
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)        
        if(self._head is None):
            self._head = newNode
        else:
            temp = self._head
            while(temp._next is not None):
                temp = temp._next
            temp._next = newNode    
        self._size += 1            
            
            
    def dequeue(self):
        if(not self.is_empty()):
            e = self._head._element
            self._head = self._head._next
            self._size -= 1                
            return e   
        return None
        
    def printQueue(self):
        temp = self._head        
        while(temp is not None):
            print(temp._element)
            temp = temp._next

        
if __name__ == '__main__':    
    print("----------Queue using Singly Linked List-----------")
    sllist = _LinkedList()
    lq = LinkedQueue(sllist)
    for i in range(0,10,2):
        lq.enqueue(i)
    sllist.printList()    
    print("---------------------")
    for i in range(0,sllist._size(),2):
        lq.dequeue()
    
    sllist.printList()
    
    print("----------Queue using inbuilt List-----------")
    q = _Queue()
    for i in range(0,10,2):
        q.enqueue(i)
    q.printQueue()    
    print("size="+str(q.size()))
    print("---------------------")
    for i in range(0,q.size(),2):
        print(q.dequeue())
    print("---------------------")
    q.printQueue()