# Que:-1)Update value of key ‘b’  by ‘banana’ where value is ‘mango’ 
# a =[{“a”: “hello”, “b”: “hii”},{“a”: “apple”, “b”: “mango”}]

# given list is:-
a=[{"a":"hello","b":"hii"},{"a":"apple","b":"mango"}]

# extracting the elements of list:-
dict1=a[0]
dict2=a[1]

# merging two dictionary into one (as we know a dictionary does not contain the same (duplicate) value,
#  so it will only print the unique key,value pairs)
appending = dict1.update(dict2)


# print(dict2)

# now updating the value of key 'b' by 'banana' 
d1={"b":"banana"}
dict2.update(d1)

# this will print the updated dictionary
print(dict2)