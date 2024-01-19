def convertinginchestocm():
    list=[150,155, 145, 148]#Declaring the list
    e=[]#empty list
    for height in list: #for loop
        e.append(height*2.54) # appending
    print("output for loop",e)
    #For list comprehension
    print("output for List Comprehension",[height*2.54 for height in list])
    
convertinginchestocm()