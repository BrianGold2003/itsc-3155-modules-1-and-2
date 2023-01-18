#exercise 3

list_1 = []
list_2 = []
x = int(input("enter an integer greater than 1:"))
for i in range(x+1):
    print(x**2)







# Get user imput for second list.
for i in range(5):
    num = int(input('Enter a number for the second list: '))
    list_2.append(num)


# Print first and sencod list
print ('First list: ',list_1)    
print ('Second list: ',list_2)


# Display the common elements in the first two list in the third list
list_3 = set(list_1).intersection(list_2)


print('Common: ', list_3)  