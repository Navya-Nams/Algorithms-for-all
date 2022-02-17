import re
patterns=['blasting','blustering',	'boasting','boosting','bootstrapping','bowstrings','bristling','busting']
text='blasting'
count=0
for i in patterns:
  if re.search(i,text):
    print("match")
    count=count+1
    print("number of matches",count)


  #if(x[1],x[4],x[5],x[7],x[8],x[9]==b,s,t,i,n,g):  
  else:
    print("no match")