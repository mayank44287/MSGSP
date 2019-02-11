#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:14:24 2019

@author: chinmay
"""
count = 0
dictCount = {}
data = [ [[10,20,30], [40, 50]],
        [[30,40,50], [10]] ]
for i in data: 
    for j in range(len(i)):
        if(10 in i[j]):
            count += 1; 
            dictCount = {10: count}
            break
    
print (dictCount)