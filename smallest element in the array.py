# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:49:59 2022

@author: J SRI THRISHNA
"""
#smallest element in the given array
arr = [25, 11, 7, 75, 56];    
   
min = arr[0];    
     
for i in range(0, len(arr)):    
      
   if(arr[i] < min):    
       min = arr[i];    
     
print("Smallest element present in given array: " + str(min)); 

# Python 3 program to find the minimum

MAX = 100

# function to find the minimum
# element of each row.
def smallestInRow(mat, n, m):
	print("{", end = "")
	for i in range(n):
		
		# initialize the minimum element
		# as first element
		minm = mat[i][0]

		for j in range(1, m, 1):
			
			# check if any element is smaller
			# than the minimum element of the
			# row and replace it
			if (mat[i][j] < minm):
				minm = mat[i][j]
		
		# print the smallest element
		# of the row
		print(minm, end = ",")

	print("}")

# function to find the minimum
# element of each column.
def smallestInCol(mat, n, m):
	print("{", end = "")
	for i in range(m):
		
		# initialize the minimum element
		# as first element
		minm = mat[0][i]

		# Run the inner loop for columns
		for j in range(1, n, 1):
			
			# check if any element is smaller
			# than the minimum element of the
			# column and replace it
			if (mat[j][i] < minm):
				minm = mat[j][i]

		# print the smallest element
		# of the row
		print(minm, end = ",")

	print("}")

# Driver code
if __name__ == '__main__':
	n = 3
	m = 3
	mat = [[2, 1, 7],
		[3, 7, 2 ],
		[ 5, 4, 9 ]];

	print("Minimum element of each row is",
								end = " ")
	smallestInRow(mat, n, m)

	print("Minimum element of each column is",
									end = " ")
	smallestInCol(mat, n, m)


