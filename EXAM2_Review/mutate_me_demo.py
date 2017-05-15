from copy import deepcopy

def mutate_me(obj1, obj2):
    '''example of how mutables and immutables work as well as [:] vs deepcopy function'''
    obj1 += 1
    list_1 = ["exam", 2]
    obj2.append(list_1)
    #obj3 = obj2[:]   # creates a deep-ish copy  
    obj3 = deepcopy(obj2)
       
    print("Nested list inside function have the same elements? ", obj3[-1]== obj2[-1])
    print("Nested list inside function have the same place in memory? ", obj3[-1] is obj2[-1], end = "\n\n")


    list_1.append(obj1)
    obj3.append("Ishida") 

    return obj3




def main():
    object_1  = 0
    object_2 = ["cyndy", 231]
    object_3 = mutate_me(object_1, object_2)


    print("\n\nIn main print statements: ")
    print(object_1)
    print(object_2)
    print(object_3)


    print("Objects outside the function have the same elements? ", object_3[:-1] == object_2)
    print("Objects outside the function have the same place in memory? ", object_3[:-1] is object_2)



main()