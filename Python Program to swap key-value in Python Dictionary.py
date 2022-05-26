#Python Program to swap key-value in Python Dictionary 
 
langdict = {'C#':1, 'C':5, 'Java':6,'Python':10,'Rust':60}
 
#swapping the keys and values
 
swappeddict={}
 
for key, value in langdict.items():
    swappeddict[value] = key
print('swapped dictionary is =\n',swappeddict)
