output = open("email.txt", "w")


emails = ""

for n,i in enumerate(open("class_lab_list.csv")):
    i = i.strip().split(",")
    email = i[2] + "; "
    emails += email
        
            
print ("# of students: ", n-1)
print(emails, file = output)


