def compare(s1,s2,n):
   if s1[:n]==s2[:n]:
      return True
   else:
      return False
s1=input("enter first string:")
s2=input("enter 2nd string:")
n=int(input("enter the number of characters:"))
print(compare(s1,s2,n))
