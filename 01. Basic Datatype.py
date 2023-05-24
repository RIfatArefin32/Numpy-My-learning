import numpy as np

#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

#introduction

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr = np.array([[1, 2], [3, 4]])
print(arr)

arr = np.array([1, 2, 3, 4], ndmin = 1)
print(arr)

arr = np.array([1, 2, 3], dtype=complex)
print(arr)

arr = np.array([12+8j, 16+9j, 13-4j], dtype=complex)
print(arr)

#Data types:
'''
bool_ (1B)
int_ (4B or 8B) intc (4B or 8B): identical of int in C
int8, int16, int32, int64
uint8, uint16, uint32, uint64
float16, float32, float64, float_ (shorthand for float64)
complex64, complex128, complex_ (shorthand for complex128)
'''
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr.itemsize)     #return the size of items in the array in Bytes

#Structure Data Type
dataType = np.dtype([('age',np.int64)]) 
print(dataType)
arr = np.array([(10), (20 ), (30 )], dtype=dataType)
print(arr)

'''
'b'         """ """  """ """boolean
'i'         (signed) integer
'u'         unsigned integer
'f'         floating-point
'c'         complex-floating point
'm'         timedelta
'M'         datetime
'O'         (Python) objects
'S','a'     (byte-)string
'U'         Unicode
'V'         raw data (void)
'''

student = np.dtype([('name', 'S'), ('roll', np.int8), ('cgpa', np.float32)])
print(student)
arr = np.array([('Rifat', 117, 3.8), ('Mahimaa', 73, 3.5)])
print(arr)
