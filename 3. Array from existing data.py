#This is used to create an array from existing data
#data could be stored as list, list of touples, touples of touples,
#or touples of lists

#numpy.asarray(a, dtype = None, order = None)

import numpy as np 
lst = [1, 2, 3, 4, 5]
arr = np.asarray(lst)
print("The array is: ", arr, "\n")

arr = np.asarray(lst, dtype = np.float_)
print("The float array: ", arr, "\n")

tpl = (1, 2, 3)
arr = np.asarray(tpl)
print("Touple as arrray: ", arr, "\n")

lst = range(5)
print(lst)
t = iter(lst)
arr = np.fromiter(t, dtype = np.float_)
print(arr)