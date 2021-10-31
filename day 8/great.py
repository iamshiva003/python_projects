def great():
    print ("hi")
    print ("hello")
    print ("world")

great()


# with arguments
def great_with_name(name):
    print (f"hello {name}")

great_with_name("shivu")


#function with more than one argument
def more(name, place):
    print (f"hello {name}")
    print (f"you from {place}")
    
more("shivu","ron")

#with positional arguments
def more(name, place):
    print (f"hello {name}")
    print (f"you from {place}")
    
more(name="shivu", place="ron")
