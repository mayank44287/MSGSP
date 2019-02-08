#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:03:02 2019

@author: mayankraj
"""

import re;

class FileProcessor:
    """takes in the input data, i.e the data file, parameter file and processe
    it to by readable by algorithm"""
    
    Data_File_Path = "DataAndParameters/data-1.txt"
    Param_File_Path = "DataAndParameters/para1-1.txt"
    
    data = []
    param = {}
    
    
    def loadData(self):
        file = open(self.Data_File_Path,'r')
        for rows in file:
            rows = rows.strip()[1:-1]
            rowdata = [[int(j) for j in re.split(',| ', s) if j != ''] for s in re.split('}{', rows[1:-1])]
            self.data.append(rowdata);
        
        for x in range(len(self.data)):
            print self.data[x]
            

if __name__ == "__main__":
    obj = FileProcessor()
    obj.loadData()