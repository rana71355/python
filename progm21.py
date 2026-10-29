words=input("enter words separated by spaces:").split()
longest=max(words,key=len)
print("longest word:",longest)
print("length of longest word:",len(longest))
