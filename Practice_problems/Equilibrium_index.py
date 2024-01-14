'''
Find Equilibrium Index of array (w.r.t EI, sum on the both side of it, becomes Equal)
'''

def eq_index(arr):
    total_sum = 0
    l = len(arr)
    for i in range(l):
        total_sum+=arr[i]
    left_sum = 0
    index = 0
    while index<l:
        right_sum = total_sum - left_sum - arr[index]
        if right_sum == left_sum:
            return index
        left_sum = left_sum + arr[index]
        index+=1