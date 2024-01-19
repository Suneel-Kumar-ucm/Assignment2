firstname=input("Enter your first name ")
lastname=input("Enter your last name ")

def fullname(your_firstname,your_lastname):
    global your_fullname
    your_fullname=your_firstname+" "+your_lastname
    print("Your fullname is " + your_fullname)
fullname(firstname,lastname)

#For displaying the alternate string 
def alternate_string(your_fullname):
    fullname=your_fullname[::2] # for showing the alternate letters
    print("The alternate string is: " ,fullname) #printing the alternate string of fullname
alternate_string(your_fullname)

