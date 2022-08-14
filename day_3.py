#3rd
"""sum1 = 0
sum2 = 0
for i in range(1,101):
    sum1+=i
    sum2+=i*i
sum1*=sum1
print(sum2-sum1)"""
#4rth
"""fl = open('upper.txt','r')
fr = open('regular.txt','w')
for i in fl:
    for j in i.split(','):
        fr.write(f'{j[0]}'+f'{j[1:].lower()}')
"""
#5th
"""num = 1310
num_copy = num
i = 0
rev = 0
while num_copy*10 % 10 != num_copy:
    num_copy = num_copy // 10
    i+=1
num_copy = num
while i>=0:
    rev+=num_copy%10 * 10**(i-1)
    num_copy = num_copy // 10
    i-=1
if num == rev:
    print(True)
else:
    print(False)"""
