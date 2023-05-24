import numpy as np

#Trigonometric function
arr = np.array([0, 30, 45, 60, 90])
sinArray = np.sin(arr*np.pi/180)
print(sinArray)

sinInv = np.arcsin(sinArray)    #returns values in radian
print(sinInv)

print(np.degrees(sinInv))   #Convert radian->degree


#Round
# numpy.around(a,decimals)
# The number of decimals to round to. Default is 0. 
# If negative, the integer is rounded to position to the 
# left of the decimal point

arr = np.array([1.0, 5.555, 12, 0.567, 25.5])
print("Original Array: ", arr)

rnd = np.around(arr)
print("After rounding: ",rnd)

rnd = np.around(arr, decimals=2)
print("Rounding at 1 decimal: ", rnd)

rnd = np.around(arr, decimals=-1)
print("Rounding at -1 decimal: ", rnd)
print()

#numpy.floor()
arr = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print("Original array: ", arr)

flr = np.floor(arr)
print("After floor operation: ", flr)

cel = np.ceil(arr)
print("After ceil operation: ", cel)


#arithmetic operation
# it is only possible if the two array are in same dimension
# or they follow broadcast rules

a = np.arange(1, 10, 1).reshape((3,3))
print("Array A:\n", a)

b = np.array([10, 10, 10])
c = np.ones(a.shape, dtype=int)

print("A+B:\n", a+b)
print("A+C:\n", a+c)

print("A*B", a*b)
print("A+b: \n", np.add(a, b), "\n")
print("A-b: \n", np.subtract(a, b), "\n")
print("A*b: \n", np.multiply(a, b), "\n")
print("A/b: \n", np.divide(a, b), "\n")


#power function:
arr = np.array([10, 100, 1000])
print("Original array: ", arr)

pow = np.power(arr, 2)
print("Power by 2: ", pow)

arr2 = np.array([1, 2, 3]) #must follow broadcast rules
pow = np.power(arr, arr2)
print("Power by arr2: ", pow)


#mod():
arr = np.array([10, 11, 100])
print("Original array: ", arr)

md = np.mod(arr, 2)
print("Mod by 2: ", md)

arr2 = np.array([2, 3, 99])
md = np.mod(arr, arr2)
print("Mod by arr2: ", md)

md = np.remainder(arr, 2)
print("Reminder by 2: ", md)

arr2 = np.array([2, 3, 99])
md = np.remainder(arr, arr2)
print("Reminder by arr2: ", md)


#Complex number:
arr = np.array([-5.6j, 0.2j, 11, 1+1j])
print("The complex aray: ", arr)
print("Real numbers are: ", np.real(arr))
print("Imaginary numbers are: ", np.imag(arr))
print("Complex conjugate: ", np.conj(arr))
print("Angle of the argument (radian): ", np.angle(arr))
print("Angle of the argument (degree): ", np.angle(arr, deg=True)) 