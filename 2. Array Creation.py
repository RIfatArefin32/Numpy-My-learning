import numpy as np

#Creating an empty array
empArray = np.empty((3, 3), dtype=np.int8)
print(empArray, "\n")



#Creating array with values 0
zeroArray = np.zeros((2), dtype=np.int8)
print("1D array: \n", zeroArray, "\n")

zeroArray = np.zeros((2, 2), dtype=np.int8)
print("2D array: \n", zeroArray, "\n")

zeroArray = np.zeros((2, 2, 2), dtype=np.float32)
print("3D array: \n", zeroArray, "\n")



#Creating array with value 1
oneArray = np.ones((2), dtype=np.int8)
print("1D array:\n", oneArray, "\n")

oneArray = np.ones((2, 2), dtype=np.int8)
print("2D array:\n", oneArray, "\n")



#Creating array full with specified value:
fullArray = np.full((2, 3), .52, dtype=np.float32)
print(fullArray)



#Creating array like another array
arr = np.array([1, 2, 3], dtype=np.int8)
print(arr, "\n")

emptyLike = np.empty_like(arr)
print(emptyLike, "\n")

zerosLike = np.zeros_like(arr)
print(zerosLike, "\n")

onesLike = np.ones_like(arr)
print(onesLike, "\n")


arr = np.zeros((2, 2), dtype=np.int32)
for i in range (arr.shape[0]):
    for j in range(arr.shape[1]):
        arr[i][j] = i+j
print(arr, "\n")

emptyLike = np.empty_like(arr)
print(emptyLike, "\n")

zerosLike = np.zeros_like(arr)
print(zerosLike, "\n")

onesLike = np.ones_like(arr)
print(onesLike, "\n")

fullArray = np.full_like(arr, 5555)
print(fullArray, "\n")



#Creating array with arange() function
#Syntax: numpy.arange(start=0, stop, step=1, dtype)
arr = np.arange(24)
print(arr)

arr = np.arange(20, 30, 2)
print(arr)

arr = np.arange(2, 20, 3, dtype=np.float_)
print(arr)

arr = np.arange(1, 2, 0.2, dtype=float)
print("The array is: ", arr, "\n")

#Creating array using shape() and reshape()
arr = np.arange(2, 13, 2)
print("Arr is: ", arr, "\n")
arr.shape = (2, 3)
print("After shaping:\n", arr, '\n')

newArr = arr.reshape(3, 2)
print("newArray: \n", newArr, "\n")
print("OldArray: \n", arr, "\n")
