# Just iterates through a range using a function to
# calculate each value.
# Uses way less memory than declaring a container
# full of values
for i in map(lambda i: i**2, range(0, 9)):
    print(i)