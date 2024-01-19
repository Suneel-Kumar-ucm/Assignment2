def wordcount(): #Declaring the function
        fileinput= open("D:\suneel_neural_network\input.txt", "r")#Getting the input file
        fileoutput= open("D:\suneel_neural_network\output.txt", "w")#Writing the outout file
        inputting_data = fileinput.readlines()#for reading the input file
        fileoutput.writelines(inputting_data)#for writing the data
        #Displaying the word count
        fileoutput.write("The word count of input file is : ")
        
        dict={}
        for i in inputting_data:# for lines
            words = i.strip().split(" ")    #for words splitting
            for j in words:
                if j in dict: 
                    dict[j] = dict[j] + 1
                else: 
            # Add the word to dictionary with count 1 
                    dict[j] = 1
  
        for key in list(dict.keys()): 
            separate= "\n" +key + " "+str(dict[key])  #to separate the word and count their occurence
            print(separate)  
        fileoutput.write(separate)
        
wordcount()
