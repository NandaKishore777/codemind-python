t=int(input())
for i in range(t):
    a=int(input())
    l=list(map(int,input().split()))
    b=sorted(l)
    c=max(l)-min(l)
    if b==l:
        print(0)
    if b!=l:
        print(c)
    