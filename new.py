import matplotlib as plt
import numpy as np



arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

arr0 = np.array(42)
print(arr0)
arr1 = np.array([1,2,3,4,5])
print(arr1)
print()
arr2=np.array([[1,2,3], [4,5,6]])
print(arr2)
print()
arr3= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,5,7]]])
print(arr3)

print()

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

print()

arr5=np.array([1,2,3,4,5], ndmin=5)
print(arr5)
print("Number of dimensions in arr5 are: ", arr5.ndim)
print()
arr = np.array([1,2,3,4,5])
print(arr[2])
print(arr[0]+arr[4])
print()

arr=np.array([[1,2,3,4,5], [6,7,8,9,10]])

print("2nd element on first row: ", arr[0,1])
print("5th element on 2nd row: ", arr[1,4])
print("Last element on 2nd dim: ",arr[1,-1])
print(arr[1:])
print()
print()
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr[0,1,2])

arr= np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[::2])
print()
arr=np.array(['apple','banana','cherry'])
print(arr.dtype)
print(arr)
arr=np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)

arr=np.array([1.1,2.2,3.3,4.1])
print(arr.dtype)
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)

print()
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=10
print(arr)
print(x)
print()

arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=10
print(arr)
print(x)
print()
arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)
print()


arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)

arr=np.array([1,2,3,4], ndmin=5)
print(arr)
print("The shape of the array is: ", arr.shape)
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)
print(newarr.base)
print()
newarr=arr.reshape(2,3,2)
print(newarr)
arr=np.array([1,2,3,4,5,6,7,8])
newarr=arr.reshape(4,2)
print(newarr)
print()

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(2,2,-1)
print(newarr)











