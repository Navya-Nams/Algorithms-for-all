# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
x=int(input("enter the number"))
y=int(input("enter the number"))
n=(len(str(y)))/2
s1=x%10**(n/2)
s2=x//10**(n/2)
s3=y%10**(n/2)
s4=y//10**(n/2)
a=s2*10**(n/2)+s1
b=s4*10**(n/2)+s3
prod=a*b
print("product",prod)

