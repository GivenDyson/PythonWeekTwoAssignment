#creating empty list
my_list = []

#appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting at index 1
my_list.insert(1, 15)

#extending my_list
my_list..extend([50, 60, 70])

#removing last element
my_list.pop()

#sorting list in ascending order
my_list.sort()

#finding and printing index 30
index_of_30 = my_list.index(30)
print("index of 30 is ", index_of_30)