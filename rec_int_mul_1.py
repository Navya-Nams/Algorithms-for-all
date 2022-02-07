x=int(input("enter the number"))
y=int(input("enter the number"))
i=10**(len(str(x))/2


a=x%i
b=x//i
e=y%i
f=y//i

c=b*i+a
d=e*i+f
prod=c*d
print("product ",prod)

