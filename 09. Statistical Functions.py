import numpy as np

#numpy.amin() and numpy.amax()

arr = np.array([[3,7,5],[8,4,3],[2,4,9]])
print("The array: \n", arr)

mn = np.amin(arr, 1)    #minimum along axis 1 (row wise)
print("minimum of along axis 1 (row): ", mn)

mn = np.amin(arr, 0)    #minimum along axis 0 (Column wise)
print("minimum of along axis 0 (Col): ", mn)

mn = np.amin(arr)
print("minimum of all: ", mn)   #minimum of all elements
print()
#same for amax()

#ptp() -> max-min value 
mn = np.ptp(arr, 1)    #max-min along axis 1 (row wise)
print("max-min along axis 1 (row): ", mn)

mn = np.ptp(arr, 0)    #minimum along axis 0 (Column wise)
print("max-min of along axis 0 (Col): ", mn)

mn = np.ptp(arr)
print("max-min of all: ", mn)   #minimum of all elements



#median
arr = np.array([[3,7,5],[8,4,3],[2,4,9]])
print("The array: \n", arr)

mn = np.median(arr, 1)    #Median along axis 1 (row wise)
print("Median along axis 1 (row): ", mn)

mn = np.median(arr, 0)    #Median along axis 0 (Column wise)
print("Median of along axis 0 (Col): ", mn)

mn = np.median(arr)
print("Median of all: ", mn)   #Median of all elements
print()


#Mean
arr = np.array([[3,7,5],[8,4,3],[2,4,9]])
print("The array: \n", arr)

mn = np.mean(arr, 1)    #Mean along axis 1 (row wise)
print("Mean along axis 1 (row): ", mn)

mn = np.mean(arr, 0)    #Mean along axis 0 (Column wise)
print("Mean of along axis 0 (Col): ", mn)

mn = np.mean(arr)
print("Mean of all: ", mn)   #Mean of all elements



# numpy.average()
# Weighted average is an average resulting from the 
# multiplication of each component by a factor reflecting 
# its importance. 
# The numpy.average() function computes the weighted average 
# of elements in an array according to their respective weight 
# given in another array. 
# The function can have an axis parameter. 
# If the axis is not specified, the array is flattened.

arr = np.array([1, 2, 3, 4])
print("The original array: ", arr)
print("The average: ", np.average(arr))

wts = np.array([4,3,2,1]) 
print("The average: ", np.average(arr, weights=wts))
print("The average and sum of weights: ", np.average(arr, weights=wts, returned=True))
print()

arr = np.array([[3,7,5],[8,4,3],[2,4,9]])
print("The array: \n", arr)

wts = np.array([3,2,1]) 
print("The average (col): ", np.average(arr, weights=wts, axis=0))
print("The average (row): ", np.average(arr, weights=wts, axis=1))
print()

#Standard daviation and variance:
arr = np.array([1, 2, 3, 4])
arr1 = np.array([[3,7,5],[8,4,3],[2,4,9]])
print("Std. daviation of arr: ", np.std(arr))
print("Variance of arr: ", np.var(arr))
print()
print("Std. daviation of arr1: ", np.std(arr1))
print("Variance of arr1: ", np.var(arr1))