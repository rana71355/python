number=list(map(int,input("enter integers separated by spaces:").split()))
result=[]
for n in number:
 if n % 2 != 0:
    result.append(n)
print("list after removing even numbers:",result)
