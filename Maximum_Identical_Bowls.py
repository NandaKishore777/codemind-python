n=int(input())
l=list(map(int,input().split()))
s=sum(l)
while n:
    if s%n==0:
        if n in l:
            k=1
            break
        if k==1:
            break
    n=n-1
print(n)