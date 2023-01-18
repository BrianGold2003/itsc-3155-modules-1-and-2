list1 = [];
list2 = [];

while True:
  y = input("Enter a number or QUIT to quit: ")
  if y == "QUIT":
    break
  list1.append(y)
print("All nums")
print(list1)

for n in list1:
  if int (n) % 2 == 0:
    list2.append(n)

print("Even nums")
print(list2)