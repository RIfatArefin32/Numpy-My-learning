import numpy as np

#Changing Shape
arr = np.arange(10).reshape((2, 5)) #reshape function
print("The reshaped array:\n",arr)

b = arr.flatten()
print("After flatten operation: ", b)

b = arr.ravel(order='C')
print("After ravel operation row major (order='C'[default]): ", b)

b = arr.ravel(order='F')
print("After ravel operation column major (order='F'): ", b)
print("After flat operation: ",arr.flat[5])
print()

#Transpose Operation
arr = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype=int)
print("The array is: \n", arr)
trans = arr.T
print("The transpose matrix: \n", trans)
print()

#swap axes operation:
arr = np.arange(1,9, 1).reshape(2,2,2)
print("The 3D array is:\n", arr)
b = np.swapaxes(arr, 1, 0)
print("After swapping 0 and 2 axes:\n",b)
print()

#split operation
arr = np.arange(9)
print(arr)
b = np.split(arr, 3)
print(b)
print(b[0])
print(b[1])
print(b[2])
x,y,z = np.split(arr, 3)
print(x)
print(y)
print(z)
print()

#array append
arr = np.array([[1,2,3],[4,5,6]])
print("The 2D array:\n", arr)

x = np.append(arr, [[7,8,9]], axis=0)
print("Append elements along axis 0: \n", x)

y = np.append(arr, [[11],[22]], axis=1)
print("Append elements along axis 1:\n", y)

z = np.append(arr, [7,8,9])
print("Append elements to the array:", z)


#insert operation: numpy.insert(arr, indx, values, axis)
arr = np.array([[1,2], [3,4], [5,6]])
print("The old array:\n", arr)
print(arr.shape)

x = np.insert(arr, 3, [7,8])
print("new array without axis: \n", x)
print(x.shape)

y = np.insert(arr, 0, [5555], axis=0)
print("Insertion along 0 axis:\n", y)
print(y.shape)

y = np.insert(arr, 0, [5555, 6666], axis=0)
print("Insertion along 0 axis:\n", y)
print(y.shape)

y = np.insert(arr, 1, [999, 9, 99], axis=1)
print("Insertion along 1 axis:\n", y)
print(y.shape)



#Delete operation: numpy.delete(arr, index/slice, axis)
arr = np.array([[1,2], [3,4], [5,6]])
print("The old array:\n", arr)
print(arr.shape)

x = np.delete(arr, 3)
print("new array without axis: \n", x)
print(x.shape)

x = np.delete(arr, np.s_[::2])
print("Using slicing: \n", x)
print(x.shape)

y = np.delete(arr, 1, axis=0)
print("Delete row 1 along axis-0:\n", y)
print(y.shape)

y = np.delete(arr, 1, axis=1)
print("Delete col 1 along axis-1:\n", y)
print(y.shape)



#Unique operation: 
# numpy.unique(arr, return_index, return_inverse, return_counts)
arr = np.array([2, 3, 4, 5, 4, 4, 9, 9])
print("The given array: ", arr)

u = np.unique(arr)
print("Unique array: ", u)

u, ind = np.unique(arr, return_index=True)
print("Unique array: ", u)
print("Indeces array: ", ind)

u, ind = np.unique(arr, return_inverse=True)
print("Unique array: ", u)
print("Inverse Indeces array: ", ind)
#reconstruct the original array:
res = np.zeros(ind.shape, dtype=int)
c = 0
for i in ind:
    res[c] = u[i]
    c += 1
print("Reconstruction the original array: ",res)

u, cnt = np.unique(arr, return_counts=True)
print("Unique array: ", u)
print("Counts: ", cnt)  #return the count of occurrance of the 
                        # elements in uniqe array


