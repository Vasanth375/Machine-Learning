import numpy as np
#importing the module
arr=np.array(
  [1, 2, 7])
#array declaration and initialisation
new=arr.astype(str)#numpy casting
#creates a new copy to new variable
print(new)#printing copy of the array
print(arr)#printing original array
print(arr.dtype)#to display the data type of arr
