#1st
"""target = [1,3,4]
def build_array(targ,n):
    counter = len(targ)
    arr = []
    for i in range(1,n+1):
        check = False
        arr.append('Push')
        for j in targ:
            if i == j:
                counter -= 1
                check = True
                continue
        if check == False:
            arr.append('Pop')
        if counter == 0:
            break
    return arr
print(build_array(target,5))"""

#2nd
"""arr1 = [5,7,5,3,9,2,3,2]
arr2 = [9,1,2,4,8,2,3]
intersection = []

for i in range(len(arr1)):
    for j in range(i+1,len(arr1)):
        if arr1[i] == arr1[j]:
            arr1[j] = None

for i in range(len(arr2)):
    for j in range(i+1,len(arr2)):
        if arr2[i] == arr2[j]:
            arr2[j] = None

for i in arr1:
    if i == None:
        continue
    for j in arr2:
        if j!= None and i==j:
            intersection.append(j)
print(intersection)"""
#3rd
#4th
"""mix = [1,2,3,4,5,6,7,8]
counter = 0
for i in range(len(mix)):
    if mix[i] % 2 == 0:
        for j in range(counter,i):
            if mix[j]%2 != 0:
                mix[i] = mix[i] + mix[j]
                mix[j] = mix[i] - mix[j]
                mix[i] = mix[i] - mix[j]
                counter+=1
                break

print(mix)"""
#5th
"""mixed = [1,2,3,1,2,5,5]
sum = 0
for i in range(len(mixed)):
    for j in range(i+1,len(mixed)):
        if mixed[j] == mixed[i]:
            mixed[i] = 0
            mixed[j] = 0
    sum+=mixed[i]
print(sum)"""
#6th
"""haystack = 'hello'
needle = 'o'
ind = 0
for i in range(len(haystack)):
    check = True
    for j in range(len(needle)):
        if haystack[i] != needle[j]:
            check = False
            break
    if check == True:
       ind = i - len(needle) + 1
print(ind)"""
#7th
str_with_spaces = 'This is a string with spaces'
print(len(str_with_spaces.split(' ')[len(str_with_spaces.split(' '))-1]))

#8th
