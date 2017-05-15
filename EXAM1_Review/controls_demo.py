
guess_me_str = input("give me a word, and i'll play around with it: ").strip()

while guess_me_str != "q":
    # basicaly keep track of the index of characters in guess_me_str
    for n, i in enumerate(guess_me_str):
        
        if i.isupper():
           # if capital letter, skip this iteration go to the next word 
            continue
            # will go out of only the for loop, because its the 
            # closest loop in enclosed by the break statement 
            #break
        else:
           print("\nThis character is not capitialized.")
        
        # if the first statement is printed, 
        # the second print statement WILL execute as well.
        print("Iteration number is: ", n) 

    guess_me_str = input("give me a word, and i'll play around with it: ").strip() 
    















