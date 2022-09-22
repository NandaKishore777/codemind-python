s=input()
s=s.split()
a=['a','e','i','o','u','A','E','I','O','U']
cnt=0
for i in s:
    if (i[0]in a) and (i[-1] not in a):
        cnt+=1
print(cnt)