# simple multiplication
a=int(input('enter the number'))
b=int(input('enter the 2 number'))
n=len(str(b))
i=1
pg=0
for i in range(n):
       c=b%10
       prod=a*c*(10**i)
       b=b-c
       b=b//(10**i)
       pg=pg+prod
       i=i+1
print("op",pg)
