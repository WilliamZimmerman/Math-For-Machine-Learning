#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:41:06 2021

@author: williamzimmerman

Inspired by Math of Machine Learning by Richard Han

A linear regression program using linear algebra for finding the best fit line/plane
"""
#Take in data points
#first fill that row with 
#transpose that
#multiply (x^tx)^-1xty which results in the value for b. That is our slope

import numpy as np
import pandas as pd 


    
def pred(x,b):
    j=0
    sum=0
    for i in b :
        print(str(i) + " " + str(x))
        if(j==0):
            sum=+i
        else:
            sum+=i*(x[j-1])
        j+=1
    print(sum)

def parsedata(inputs):
    xiter=0#so we can loop through all x inputs
    
    appendval=[1.0]
    while(xiter<len(inputs)-1):#loop through all but output value
        appendval.append(float(inputs[xiter]))#a vector we can use
        xiter+=1#to iterate
    return appendval
        

def linreg(choice):
   xMat = []
   yVec =[]#array
   if choice==1:
       while(True):
       
        inString= input("please enter the data points \nEmpty input means done with data")
        if(inString==""):#sentinel
            break
        inputs =inString.split(',')#split into individual numbers
        appendval=parsedata(inputs)
       
        xMat.append(appendval)#add to matrix
       
        yVec.append(float(inputs[-1]))#add to vector
        
   elif choice==2:
        filename=input("plese enter the path to the file")
        file1=open(filename, 'r')
        lines = file1.readlines()#create a list of lines
        for line in lines:
            inputs=line.split(',')#split to seperate numbers
            appendval=parsedata(inputs)
            xMat.append(appendval)#add to matrix
            
            yVec.append(float(inputs[-1]))#add to vector
            
        
   
    

   yVec=np.array(yVec)#so we can use np functions
   yVec = np.reshape(yVec, -1)#reshape into vector form
   transpose = np.transpose(xMat)
   xSquare = np.matmul(transpose,xMat)#find square matrix
   if(np.linalg.det(xSquare)==0):#to avoid an error
        print("error 0 determinant")
   else:
        xSquare = np.linalg.inv(xSquare) #invert the matrix and the transpose
        b=np.matmul(xSquare, transpose)#multiply the new inverse by the transpose
        b=np.matmul(b,yVec)#multiply this current value by the yvector
        print(b)
    
   j=0
   print("best fit model is: ")
   for i in b:
        if(j==0):
            print(str(i) + " + ")
        elif(j==len(b)):
            print(str(i) + "x" + str(j))
        else:
            print(str(i) + "x" + str(j))
    
        j+=1
    
   choice = input("What value(s) would you like to find an estimate for?")
    
   inputs=choice.split(',')
    
   pred([float(i) for i in inputs],b)

def main():
    choice = int(input("Would you like to enter data \n1. manually\n2.Via Text file"))
    linreg(choice)

if  __name__ == "__main__":
    main()
    

