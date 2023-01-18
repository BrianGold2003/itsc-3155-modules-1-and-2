# Get  a string from user
x = input("Enter a string: ")


# Create an emty list
y = list(x)
z = []


# Split the list of characters into a list of lists with 3 elements each
for i in range(0, len(y),3):
    a = []
    for k in range(0,3):
        if(i+k)< len(y):
            a.append(y[i+k])
    z.append(a)
print(z)