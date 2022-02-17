#program to find number of zabs born
a=int(input("enter the number of zab born in this year"))
b=int(input("enter the number of zab born last year"))
d=int(input("enter the this year"))
c=0
count=0
while(c!=1):
  c=abs(a-b)+1
  a=b
  b=c
  print(c)
 
  count=count+1
  
print("enter the number ",count)
year=count+d
print("the year is",year)
