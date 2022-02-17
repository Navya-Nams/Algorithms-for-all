# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def fun(a,b):
  return a*b

x=int(input("enter the number"))
y=int(input("enter the number"))
n=(len(str(y)))/2
a=x%10**(n/2)
b=x//10**(n/2)
c=y%10**(n/2)
d=y//10**(n/2)
prod=(10**n)*fun(b,c)+(10**(n/2))*fun(b,d)+(10**(n/2))*fun(a,c)+fun(a,d)
print("product",prod)

