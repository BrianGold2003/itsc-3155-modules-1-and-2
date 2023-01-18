list1 = []
list2 = []

for x in range(10):
  y = input("Enter a number: ")
  list1.append(y)

print("Original list: ", end = '')
print(list1)

for n in list1:
  if (list1.count(n) == 1):
    list2.append(n)

print("Numbers That appear once: ", end = '')
print(list2)