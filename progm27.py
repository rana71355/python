n=int(input("enter the number of items:"))
number=[]
for i in range(n):
   num=int(input("enter a number:"))
   number.append(num)
   total=0
for i in number:
   total=total+i
print("sum=",total)
