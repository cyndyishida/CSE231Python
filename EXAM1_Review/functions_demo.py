def function1 (var_1, var_2): 
    " function returns first parameter to the power of the second parameter"
    # this is a local namespace for function 1
    print("first value given is :", var_1, " and second value given is :", var_2)
    return var_1 ** var_2




# this is the main namespace

var_1 = 3 
var_2 = 2

var_3 = function1(2,3)
print("For the first value, the return statement is: ", function1(var_2, var_1))
# prints 9 or 8?? 
# answer is 8









'''
Example of the difference of local and Global Scope
You can call variables whatever you want, what you pass in to the function
is what the interpreter will view inside the function,
in this example even though I named the variables the same,
2 is the first parameter of the function & 3 is the second, regardless of anything else.
'''