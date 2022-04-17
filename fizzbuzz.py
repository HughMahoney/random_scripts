"""
My solution to fizzbuzz - do not use in any professional setting as it would be obnoxious.
"""
#I wonder why the list is in that order?
output = ["fizzbuzz", "buzz", "fizz"] 

#I wonder why the list is in that order? Its not related to output obviously.
iterList = lambda x: [x%i for i in [15, 5, 3]]

#Not gonna use the order of the list to create the list totally - that would be non-functional right?
fizzbuzz = [output[iterList(x).index(0)] if 0 in iterList(x) else x for x in range(1, 101)]
print(fizzbuzz)
