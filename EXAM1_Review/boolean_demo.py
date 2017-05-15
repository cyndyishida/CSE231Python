user_str = input("input a value to be booleaned: ").strip()

# when I press enter, both statements print the else block
# anything else prints inside the if block

if user_str or False:
    print("This statement is true, basically user_str is not null!")
else:
    print("This conditional was false for the or.\n\n")


if user_str and True:
    print("This 'and statement' executed as true!")
else:
    print("This conditional was false.")