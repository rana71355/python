text=input("enter a line a text:")
words=text.split()
count={}
for words in words:
 if words in count:
     count[words]+=1
 else:
      count[words]=1
print(count)
