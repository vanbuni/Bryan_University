#define a function

# def func1():
#     print("I am learning Python Functions")
#     print("Still in func1")

# func1()

# def square(x):
#     return x*x
# print(square(4))

# def multiply(x,y=0):
#     print("Value of x=", x)
#     print("Value of y=", y)

#     return x*y

# print(multiply(y=2,x=4))


#Lambda

# adder = lambda x, y: x + y
# print(adder (1,2))


#What a lambda returns

# string= 'some kind of useless lambda'
# print(lambda string : print(string))


#What lambda returns # 2
# x = 'some kind of useless lambda'
# (lambda x : print(x))(x)


#Lambda filters

# sequences = [10,2,8,7,5,4,3,11,0,1]
# filtered_result = filter (lambda x: x > 4, sequences)
# print(list(filtered_result))

# lambda map
# sequences = [10,2,8,7,5,4,3,11,0,1]
# filtered_result = map (lambda x: x*x, sequences)
# print(list(filtered_result))


# #lambda reduce


# from functools import reduce
# sequences = [1,2,3,4,5]
# product = reduce (lambda x, y: x*y, sequences)
# print(product)