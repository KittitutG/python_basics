my_list = ["apple", "banana", "cherry"]

print(my_list[0],my_list[1],my_list[2]) #List starting from 0
#expect output apple,banana,cherry
print('--------------------')
# negative index
print(my_list[-1]) #reversal order
# expect output is cherry
print('--------------------')

# index range
print(my_list[1:2]) #get item starting from 1 till 2
# expect output is banana as a list of string
print('--------------------')

# by leaving empty, this mean either getting from start/end
print(my_list[:1],': should retun from start till item1')
# expect output is apple
print(my_list[1:],': should retun from item1 till end of lis')
# expect output is banana, cherry 


# update element
my_list[1] = 'watermelon'
print(my_list)

# update range of item
my_list[:2] = 'vanilla','coffe'
print(my_list)


#append() item
my_list.append('coke')
print(my_list)

#insert() on specific index
my_list.insert(3,'pepsi')
print(my_list)

#extend() list from other list
oth_list = ['car','bus','van']
my_list.extend(oth_list)
print(my_list)
print('-------------------------')
# extend() also applied with other Iterator object
tup_obj = ('obj1','obj2')
print('tup_obj type is, ', type(tuple), 'existing list object type is', type(my_list))
my_list.extend(tup_obj)
print(my_list,'----------',type(my_list))
