d={}
n=int(input("enter number of items:"))
for i in range(n):
   key=input("enter key:")
   value=int(input("enter value:"))
   d[key]=value
ascending=dict(sorted(d.items(),key=lambda item:item[1]))
descending=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
print("Ascending order:",ascending)
print("descending order:",descending)
