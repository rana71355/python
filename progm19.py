string=input("enter a string:")
for ch in string:
  if string.index(ch)==string.find(ch):
     print(ch,":",string.count(ch))
