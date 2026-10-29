numbers=list(map(int,input("enter integers separated by spaces:").split()))
positive=[n for n in numbers if n>0]
print("positive numbers:",positive)

n=int(input("enter N:"))
squares=[i*i for i in range(1,n+1)]
print("squares:",squares)

word=input("enter a word:")
vowels=[ch for ch in word if ch.lower() in "aeiou"]
print("vowels:",vowels)

word=input("enter a word:")
values=[ord(ch) for ch in word]
print("ordinal values:",values)
