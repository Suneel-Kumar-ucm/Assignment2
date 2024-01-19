firstname=input("Enter your first name ") #for entering first name
lastname=input("Enter your last name ") # for entering lastname
#function for fullname
def fullname(your_firstname,your_lastname):
    global your_fullname
    your_fullname=your_firstname+" "+your_lastname #combining the first and last name
    print("Your fullname is " + your_fullname) #printing the fullname
fullname(firstname,lastname) #calling the fucntion