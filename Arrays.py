'''Rotate an array using the reversal algorithm
-> Reverse A to get ArB where Ar is reverse of A
-> Reverse B to get ArBr where Br is reverse of B
-> Reverse all to ger (ArBr)r=BA

Let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7 
A = [1, 2] and B = [3, 4, 5, 6, 7] 
 
Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]

'''
#function to revrse array from index start to end
def reverseArray(arr, start, end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end=end-1

#fuction to rotate left the array of size n by d
def leftRotate(arr,d):
    if d==0:
        return
    n=len(arr)
    d=d%n
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1)

#function to print 
def printArray(arr):
    for i in arr:
        print(i, end=' ')

#driver code to test the above fnction
arr=[1,2,3,4,5,6,7]
n=len(arr)
d=2

leftRotate(arr,d)
print(arr)
