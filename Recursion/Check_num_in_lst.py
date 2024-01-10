# Check Number in list or not

def checknum(arr, n):
    l = len(arr)
    if l == 0:
        return False
    if arr[0]==n:
        return True
    smallarray = checknum(arr[1:], n)
    return smallarray

li = [1,2,3,4,5,6,7]
print(checknum(li, 4))