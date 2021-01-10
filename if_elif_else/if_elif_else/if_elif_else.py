tall=int(input("How tall are you?: "));
print(tall)
if tall >= 120:
  age=int(input("Age? "))
  if age <= 12:
    print("Please pay 12.")
  elif age<20:
    print("Please pay 17 $");
  else:
    print("Please pay 20 $");
else:
    print("You should grow little taller to ride a rollercoaster!");