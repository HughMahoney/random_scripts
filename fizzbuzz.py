"""
My first solution to fizzbuzz - do not use in any professional setting as it would be obnoxious.
"""
#I wonder why the list is in that order?
output = ["fizzbuzz", "buzz", "fizz"] 

#I wonder why the list is in that order? Its not related to output obviously.
iterList = lambda x: [x%i for i in [15, 5, 3]]

#Not gonna use the order of the list to create the list totally - that would be non-functional right?
fizzbuzz = [output[iterList(x).index(0)] if 0 in iterList(x) else x for x in range(1, 101)]
print(fizzbuzz)

"""
My one line solutiont to fizzbuzz - better maybe?

"""
#List comprehension is cool, until you have a million if statements.
fizzbuzz = ["fizzbuzz" if x%15==0 else "buzz" if x%5==0 else "fizz" if x%3==0 else x for x in range(1,101)]
print(fizzbuzz)

"""
Most functional solution? Because it can extend beyong just fizzbuzz
"""
div_dict = [(15, "fizzbuzz"), (5, "buzz"), (3, "fizz")]
fizzbuzz = []
for i in range(1, 101):
  fizzbuzz.append(i)
  for div in div_dict:
    if i%div[0] == 0:
      fizzbuzz[i-1] = div[1]
      break
print(fizzbuzz)

"""
retrospectively, this can be shortened even further, because 3, 5 are prime constituents of 15.
"""
