str1 = input("Please Enter your Own String : ")

str2 = ''

for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
        
print("Original String :  ", str1)
print("Final String :     ", str2)
