# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 07:01:03 2022

@author: J SRI THRISHNA
"""

def linear_search(list,n,key):
    for i in range(0,n):
        if (list[i]==key):
            return i
    return -1

list=eval(input())
key=int(input())
n=len(list)
res=linear_search(list,n,key)
if (res==-1):
    print("Element not found")
else:
    print("Element found in",res)
    
    
def binary_search(list,n):
    low=0
    high=len(list)-1
    mid=0
    
    while(low<=high):
        mid=(low+high)//2
        if list[mid]<n:
            low=mid+1
        elif list[mid] > n:
            high=mid-1
        else:
            return mid
    return -1

list=eval(input())
n=int(input())
result=binary_search(list,n)
if (result!=0):
    print("element found at",str(result))
else:
    print("element not found")