# mutable, allows duplicates, dynamic array 'arraylist' in Java, can store different types of
# data in same list. It is ordered by default. 

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

print(type(a))

newList = list(("apple", "banana", "cherry"))#make new with list()
print(newList)
