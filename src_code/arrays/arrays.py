# mutable, allows duplicates, dynamic array 'arraylist' in Java, can store different types of
# data in same list. It is ordered by default. 

# creating a list 

a = [0,1,2,3,4,5,6,7,8,9]
print(a)

b = [False,'#', 0.5,20,'hi']
print(b)

# creating an n-dimensial list
nArr = [[0,1,2],[3,4,5],[6,7,8]]
print("\nmulti-dimensional list: ")
print(nArr)

print(nArr[1][1]) #print the middle item
print(a[-2]) #print second last item
print(len(nArr))

print(type(a[4])) #print type of element

newList = list(("apple", "banana", "cherry"))#make new with list()
print(newList)

# Create a list [0, 0, 0, 0, 0, 0, 0]
eightElementArr = [0] * 7
print(eightElementArr)

# Modifying the elements in existing list
# https://www.geeksforgeeks.org/python-lists/

emptyList = []

# adding to a list: 

# append() add an element to end of the list
emptyList.append('a')
print(emptyList)
# extend(): add multiple elements to the end of list
emptyList.extend(['i','u','e','o'])
print(emptyList)
# insert(): add element to specific index, inserting  at index 0
emptyList.insert(0, 'Vowels: ')
print(emptyList)





