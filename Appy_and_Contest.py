for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    k=a//b
    l=a//c
    v=max(b,c)
    q=min(b,c)
    i=1
    while True:
        if v%q==0:
            break
        v=v*i
        i+=1
    z=a//v
    if (k+l-z)>=d:
        print('Win')
    else:print('Lose')
    