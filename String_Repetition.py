s=input()
n=int(input())
if n>len(s):
    a=n//len(s)
    c=s.count('a')
    d=a*c
    d+=s[:n%len(s)].count('a')
    print(d)
else:
    print(s[:n].count('a'))