#from __future__ import print_function
string = 'abc'
print((string * 2))
#result=abcabc

arr = [1, 2, [3, 4], 'a', 'b']
print((arr[4:0:-2]))
#The above code will print:
#['b', [3, 4]]
#This is because of the numbers we specify in the list indexing: 
#arr[4:0:-2]
#The 4 specifies the starting index in the list which is the end of the list, the 0 specifies the ending index of the list, and the last -2 specifies how to step through the array. Putting this all together, we get start from the 4th index position, go up to the 0th index position, and get every second element going backwards in the list.

string = "abc cde"
print((list(string)))
# => ['a','b','c',' ','c','d','e']

#The xrange function will produce an error, the split function by default splits a string into a list of words so that answer is pretty close, and the set function creates a list of unique characters so for the string above the 'c' character would only appear once if we used the set function.

a = [x**2 for x in range(4)]
print(a)


def foo(num):
	a, b = 1, 1
	while b < num:
		a, b = b, a + b
	return b == num
print(foo(13))

