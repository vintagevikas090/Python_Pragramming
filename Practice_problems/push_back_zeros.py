'''
You have been given a random integer array/list(ARR) of size N. 
You have been required to push all the zeros that are present in the array/list to the end of it. 
Also, make sure to maintain the relative order of the non-zero elements.
'''

l = [3,66,0,0,323,5,7,9]
pos = 0
for i in range(len(l)):
    if l[i]!=0:
        l[pos]= l[i]
        pos+=1
while pos<len(l):
    l[pos]= 0
    pos+=1
print(l)