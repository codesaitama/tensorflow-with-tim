import numpy as np

rolls = np.random.randint(low=1, high=6, size=10)

# print(rolls)
# print(rolls <= 3)
# print(rolls + 10)

xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = np.asarray(xlist)

print("xlist = {}\nx = {}\n".format(xlist, x))
print(f'xlist = {xlist}\nx = {x}')

print(xlist[1][-1]) # Get the last item from the second array in the two dimensional array.