"""f = open('numbers.txt', 'r')
sum = 0
for line in f.readlines():
    for element in line.split(' '):
        sum+=int(element)
print(sum)"""

"""f1 = open('random_text.txt','r')
f2 = open('another_text.txt','w')

for line in f1.readlines():
    counter = 1
    for element in line.split(' '):
        f2.write(f'{element[0].upper()}'+f'{element[1:]}  ')
    counter+=1
    if counter == len(line.split(' ')):
        f2.write('\n')

f1.close()
f2.close()
f2 = open('another_text.txt','r')
for i in f2.readlines():
    print(i)
f2.close()"""


#3rd
"""dic = {}
rand_lis = [1,2,3,3,2,1,1,2]


for i in rand_lis:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1
print(dic)"""

#4rth
"""fl = open('random_text.txt','r')
elem = 0
for line in fl.readlines():
    for word in line.split(' '):
        for element in word:
            elem+=1
print(elem)"""

#5th
"""str1 = 'abcd'
str2 = ''
for i in range(len(str1)):
    if i == 2:
        continue
    str2+=str1[i]
print(str2)"""

#6th
"""fil = open('random_text.txt','r')
words = []
rep = []

for line in fil.readlines():
    for word in line.split(' '):
            words.append(word)

for i in range(len(words)-1):
    rep.append(0)
    for j in range(i+1,len(words)):
        if words[j] != -1 and words[i]==words[j]:
            rep[i]+=1
print(rep)"""

#7th
"""lis1 = [1,2,3,4,5]
lis2 = []
for i in lis1:
    lis2.append(i*i)
for j in range(len(lis2)-1):
    for k in range(j+1,len(lis2)):
        if lis2[j] > lis2[k]:
            lis2[k] = lis2[j] + lis2[k]
            lis2[j] = lis2[k] - lis2[j]
            lis2[k] = lis2[k] - lis2[j]
print(lis2)"""
#8th
"""num = 7485
sum = 0

while num*10%10!=num:
    sum+=num%10
    num = num//10
print(sum)"""
#9th
"""num = 7485
product = 1
sum = 0
while num*10%10!=num:
    product*=num%10
    sum+=num%10
    num = num//10
delta = product-sum
print(delta)"""
#10th
"""a = 1
b = 11
odd = 0
for i in range(a,b+1):
    if i%2 != 0:
        odd+=1
"""

