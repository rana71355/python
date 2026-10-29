def simple_interest(p,t,senior):
   if senior=="yes":
      r=12
   else:
      r=10
   si=(p*r*t)/100
   return si
p=float(input("enter the principle amount:"))
t=float(input("enter the time in years:"))
senior=input("is the customer a senior citizen?(yes/no):")
interest=simple_interest(p,t,senior.lower())
print("simple_interest=",interest)
