#LISTS IN PYTHON


#creating list:

name_list=["Mark", "Anthony", "Joe", "Mike", "Nathan"]
print(name_list)

#print out just some elements of lists

print(name_list[2])   #list index start with 0

#adding elements to the end of the list

name_list.append("Bumblebee")
print(name_list)

#adding element between two places of list

name_list.insert(2, "Bomb")
print(name_list)

#pop the element from selected index
name_list.pop(2)
print(name_list)

