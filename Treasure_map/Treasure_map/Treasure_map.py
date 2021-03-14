#TREASURE MAP- Put the x where the treasure is...
row1 = ["0","0","0"]
row2 = ["0","0","0"]
row3 = ["0","0","0"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
print(position)
row=int(position[0])
column=int(position[1])
if row>3 or column>3:
    print("Coordinates must be lower then 3!")
    quit()
print(row, column, end="\n")

map[row-1][column-1]="X"


print(f"{row1}\n{row2}\n{row3}")
