# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:53:13 2020

@author: Gunjan
"""

class _Node:
    __slots__='_element','_next'

    def __init__(self,element):
        self._element = element
        self._next = None
    
class _LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def _size(self):
        return self.size
    
    def isEmpty(self):
        if(self.head is None):
            return True
        else:
            return False
    
    def printList(self):
        temp = self.head
        while(temp is not None):
            print(temp._element)
            temp = temp._next
    
    def first(self):
        return self.head
    
    def last(self):
        temp = self.first()
        last = temp
        while(temp is not None):
            last = temp
            temp = temp._next            
        return last

    # def after(self, n):
    #     temp = self.head
    #     while(temp is not None):
    #         if(temp == n):
    #             break;
    #         temp = temp._next
    #     if(temp is not None):    
    #         return temp._next    
    #     else:
    #         return None
    
    # def before(self, n):
    #     temp = self.head
    #     prev = temp
    #     while(temp is not None):            
    #         prev = temp
    #         if(temp._element == n._element):
    #             break;
    #         temp = temp._next
    #     return prev
    
    def insertFirst(self, element):
        newNode = _Node(element)
        if(self.head is None):
            self.head = newNode
        else:
            newNode._next = self.head
            self.head = newNode
        self.size += 1            
    
            
    def insertLast(self, element):
        newNode = _Node(element)
        last = self.last()
        if(last is not None):
            last._next = newNode
        else:
            self.head = newNode
        self.size += 1            
            
    def search(self, element):
        temp = self.first()
        while(temp is not None):
            if(temp._element == element):
                return temp                
            temp = temp._next            
        return None

    def remove_first(self):
        if(self.first() is None):
            print("List is empty")
        else:
            temp = self.head._next
            self.head = temp
        self.size -= 1            
    
    def remove_last(self):
        temp = self.first()
        prev = temp
        while(temp._next is not None):    
            prev = temp
            temp = temp._next
        prev._next = None    
        self.size -= 1            
            
    def insertBefore(self, curr_element, new_element):
        m = self.first()
        while(m._next is not None):            
            if(m._next._element == curr_element):
                print("inside")
                newNode = _Node(new_element)
                newNode._next = m._next
                m._next = newNode
                self.size += 1
                break
            m = m._next
                
                
if __name__ == '__main__':
    sllist = _LinkedList()
    for i in range(0,10,2):
        sllist.insertLast(i)
    sllist.insertFirst(23)    
    sllist.insertLast(323)  
    sllist.insertBefore(2,34)
    sllist.printList()
    print("--------------------")
    sllist.remove_first()    
    sllist.remove_last()    
    sllist.printList()
    search=sllist.search(213)
    print(search._element if search is not None else "data not found" )
    print("size="+str(sllist._size()))
    print("isEmpty="+str(sllist.isEmpty()))    