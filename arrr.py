# # importing array module
# import array as arr
 
# # array with int type
# a = arr.array('i', [1, 2, 3, 4, 5, 6])
 
# # accessing element of array
# print("Access element is: ", a[0])
 
# # accessing element of array
# print("Access element is: ", a[3])
 
# # array with float type
# b = arr.array('d', [2.5, 3.2, 3.3])
 
# # accessing element of array
# print("Access element is: ", b[1])
 
# # accessing element of array
# print("Access element is: ", b[2])


# def sum_all(*args):
    # sum = 0
#     for i in args:
#         sum+=i
#     print("Answer is :", sum)

# sum_all(2,2,9,9,0)

# exec('a=5;b=6;a,b=b,a;print(a,b)')


# # Function to take multiple arguments
# def add(datatype, *args):

# 	# if datatype is int
# 	# initialize answer as 0
# 	if datatype =='int':
# 		answer = 0
		
# 	# if datatype is str
# 	# initialize answer as ''
# 	if datatype =='str':
# 		answer =''

# 	# Traverse through the arguments
# 	for x in args:

# 		# This will do addition if the
# 		# arguments are int. Or concatenation
# 		# if the arguments are str
# 		answer = answer + x

# 	print(answer)

# # Integer
# add('int', 5, 6)

# # String
# add('str', 'Hi ', 'Geeks')

