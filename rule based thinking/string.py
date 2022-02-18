#to check the string #text='b??st*ing'
import re
patterns=['b2astyuining','blustering',	'boasting','boosting','boostrapping','bowstrings','bristling','busting']
#text='\b{2}st*ing'
count=0
for i in patterns:
  reg=re.search('^b..st.*ing$',i)
  print(reg)
  if reg==None:
    print("no match",i)

  elif reg.group(0):
    print("match",i)
    count=count+1
    print("number of matches",count)


  
    