# Tuple Negative Numbers

negTuple = (3, -8, -22, 4, -98, 14, -33, -78, 11)
print("Negative Tuple Items = ", negTuple)

print("\nThe Negative Numbers in negTuple Tuple are:")
for i in range(len(negTuple)):
    if(negTuple[i] < 0):
        print(negTuple[i], end = "  ")
