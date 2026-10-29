d1={}
d2={}
n1 =int(input("enter number of items in dictionary 1:"))
for i in range(n1):
   key=input("enter key:")
   value=input("enter value:")
   d1[key]=value
n2 =int(input("enter number of items in dictionary 2:"))
for i in range(n2):
   key=input("enter key:")
   value=input("enter value:")
   d2[key]=value
   
d1.update(d2)
 
print("merged dictionary:",d1)
