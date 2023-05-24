import numpy as np

arr = np.arange(10)
slc = slice(2, 8, 2)    #start, stop, step
print(arr[slc])
print()

#we can perfrom same operation directly
b = arr[2:7:2]
print(b)
print()

print(arr[5])
print(arr[1:5])
print(arr[1:])
print(arr[:5])
print(arr[:])
print()

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr)
print(arr[1:])
print()

print("The array is: \n", arr, "\n")
print("The items of the 0th row: ", arr[0, ...])
print("The items of the 1th row: ", arr[1, ...])
print("The items of the 0th column: ", arr[..., 0])
print("The items of the 1st row: ", arr[..., 1])
print("The array of 1st and others rows: \n", arr[1:,...])
print()

print("The items greater than 2:", arr[arr>2])
print("The even items:", arr[arr%2==0])

a = np.array([1, 2+6j, 5, 3.5+5j]) 
print("Complex numbers: ", a[np.iscomplex(a)])

