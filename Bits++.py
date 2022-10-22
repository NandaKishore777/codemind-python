d=0
for i in range(int(input())):
    s=input()
    
    if '+' in s:
        d+=1
    else:
        d-=1
    
print(d)