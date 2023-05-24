import numpy as np

a = 13
b = 17

print("Binary of 13 is: ", bin(a))
print("Binary representation of 13 is: ", np.binary_repr(a))
print("Binary representation of 17 with width 8: ", np.binary_repr(b, width=8))



print ("inversion of 13: ",np.invert(a)) 
print ("inversion of 13 in integer: ",np.invert(a, dtype=np.int8))
print ("inversion of 13 in unsigned integer: ",np.invert(a, dtype=np.uint8)) 
print("Bitwise and: ", np.bitwise_and(a, b))
print("Bitwise or: ", np.bitwise_or(a, b))
print("Bitwise xor: ", bin(np.bitwise_xor(a, b)))
print("Before left shift: ", np.binary_repr(10, width=8))
x = np.left_shift(10, 2)
print("Shifted integer: ",x)
print("After left shift: ", np.binary_repr(x, width=8))
print("Before right shift: ", np.binary_repr(10, width=8))
x = np.right_shift(10, 2)
print("Shifted integer: ",x)
print("After right shift: ", np.binary_repr(x, width=8))

