# 2) print  ‘hi’ when pass to all objects of the list but in case of ‘d’ print ‘good morning’
# a= [‘z’, ‘b’, ‘h’, ‘r’, ‘j’, ‘d’, ‘k’, ‘m’]

# function to print "good morning message" and "hi" with certain condition.
def func1(arr):

    # loop will run untill all the items of list are not visited.
    for item in range(len(arr)):

        # if statement will print "good morning" only if list element is "d".
        if arr[item]=='d':
            print('good Morning')

        # else it will continue printing hii
        else:
            print('hi')

# given list with some values
a=['z', 'b', 'h', 'r', 'j', 'd', 'k', 'm']

# calling of a function 
func1(a)