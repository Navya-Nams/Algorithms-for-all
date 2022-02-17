# digit containing all even number
num=int(input("enter the number"))
c=num
while(num>=1):
  if(num%2)==0:
    a=int(num//10)
    num=a 
  else:
    num=2*c
    c=num
print("The even number is",c)
