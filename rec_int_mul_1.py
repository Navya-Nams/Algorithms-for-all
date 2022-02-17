def fun(x,y,n):
  return x*y*n/2


x=int(input("enter the number"))
y=int(input("enter the number"))

n=(len(str(y)))/2

x1=x%10**(n/2)
x2=x//10**(n/2)
y1=y%10**(n/2)
y2=y//10**(n/2)
prod=10**n*fun(x1,y1,(n/2))+10**(n/2)*fun(x1,y2,(n/2))+10**(n/2)*fun(x2,y1,(n/2))+fun(x2,y2,(n/2))


print("product",prod)




