rows = int(input("Enter Half Diamond Pattern Rows = "))

print("Half Diamond Pattern") 
i = 0
while(i <= rows):
    j = 0
    while(j < i):
        print('*', end = '')
        j = j + 1
    i = i + 1
    print()

i = 1
while(i < rows):
    j = i;
    while(j < rows):
        print('*', end = '')
        j = j + 1
    i = i + 1
    print()
