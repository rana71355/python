start=int(input("enter start:"))
end=int(input("enter end:"))
for n in range(start,end+1):
   if 1000<=n<=9999 and all(int(d)%2==0 for d in str(n)):
      r=int(n**0.5)
      if r*r==n:
          print(n)
