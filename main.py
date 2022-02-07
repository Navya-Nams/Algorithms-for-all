
a=int(input('enter the number'))
b=int(input('enter the 2 number'))
n=len(str(b))
i=1
pg=0
#while(i<=n):
for i in range(n):
       c=b%10
       #print("the",c)
       prod=a*c*(10**i)
       #print("prod",prod)
       b=b-c
       b=b//10
       #print("after",b)
       pg=pg+prod
       i=i+1
print("op",pg)
