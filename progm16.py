color_list1=input("enter colors for list1:").split(",")
color_list2=input("enter colors for list2:").split(",")
print("colors not present in list2:")
for color in color_list1:
  if color not in color_list2:
     print(color)
