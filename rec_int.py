def fun(x,y,n):

  if n==1:
    return x*y
  
  else:
  
    x2=x%(10**(n/2))
    x1=(x-x2)/(10**(n/2))
    y2=y%(10**(n/2))
    y1=(y-y2)/(10**(n/2))

    prod=(10**n)*fun(x1,y1,n/2)+(10**(n/2))*fun(x1,y2,n/2)+(10**(n/2))*fun(x2,y1,n/2)+fun(x2,y2,n/2)
    #print("product",prod)
    
    return prod

  
def main():
  if __name__=="__main__":
    main()
  

x=int(input("enter the number"))
y=int(input("enter the number"))
n=len(str(y))

prod=fun(x,y,n)

print("product",prod)
  



