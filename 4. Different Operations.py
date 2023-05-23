import numpy as np
#element to element operation: Note: The dimension must be same

a1 = np.array([1, 2, 3, 4], dtype=int)
a2 = np.array([5, 6, 7, 8], dtype=int)
print("The sum of two array: ", a1+a2)
print("The sub of two array: ", a1-a2)
print("The mul of two array: ", a1*a2)
print("The div of two array: ", a1/a2)
print()

a1 = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=int)
a2 = np.array([[7,8,9],[4,5,6],[1,2,3]], dtype=int)
print("The sum of two array: \n", a1+a2)
print("The sub of two array: \n", a1-a2)
print("The mul of two array: \n", a1*a2)
print("The div of two array: \n", a1/a2)
print()


#Broadcasting Operation:
a = np.array([[0,0,0],[1, 1, 1],[2, 2, 2],[3, 3, 3]]) 
b = np.array([1, 2, 3])  
   
print('First array:\n', a)
   
print('Second array:\n', b)
   
print('First Array + Second Array:\n', a+b)


#Matrix transposition
a = np.array([[1, 1, 1],[2, 2, 2],[3, 3, 3]])
b = a.T
print(b)


#Scaler multiplication
a = np.array([1, 2, 3, 4, 5])
a = 2*a
print(a)
