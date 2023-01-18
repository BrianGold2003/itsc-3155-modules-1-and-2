list1 = []
for x in range(5):
  y = input("Enter a word: ")
  list1.append(y)

print("Words: ", end ='')
print(list1)

a = " ".join(list1)
print(a)