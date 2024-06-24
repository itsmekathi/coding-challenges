""" 
This solution uses the plan brute force method
using the 2 pointer approach, here we are not 
using indexes so if repetative numbers are present
the results might differ, so we might need to swith to
a pointer based approach
operational complexity O(n^2) since it loops over the array twice.
"""

data = [10, 15, 3, 7]
k = 25

for i in data:
    for j in data:
        if i == j:
            continue
        sum = i + j
        if sum == k:
            print ('num1 = ', i ,' num 2 = ', j)
            print('Sum exists for numbers')
            break
