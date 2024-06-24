""" 
This solution uses the in place differenciation approach
Operational effiency O(n) since it loops over the array once.
"""

data = [10, 15, 3, 7]
k = 25

diff = 0
for i in range(0, len(data)):
    temp_diff = k - data[i]
    if temp_diff == 0:
        print('Sum exists.. exiting')
        break
    if temp_diff > 0:
        diff = temp_diff
        continue
