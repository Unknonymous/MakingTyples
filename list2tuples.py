my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#Dictionary above was copied from the learning platform per the assignment instructions
# Expected Output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def tuplfy(tiona):                                   #setting the function name
    print tiona.items()                              #called the items() function that outputs the proper list of tuples

#tuplfy(my_dict)                                     #called the defined function

def tuplfy2(tiona):                                  #building the built-in function
    tuplist = []                                     #initalizing the list of tuples
    for i in range (0, len(tiona)):                  #looping through the dictionary
        tuplist += [(tiona.keys()[i],tiona.values()[i])]       #adding key, value pairs to the list as tuples
    print tuplist                                              #printing the built list

tuplfy2(my_dict)                                     #calling the defined function