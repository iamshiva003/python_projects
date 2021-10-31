def add(a,b):
    return f"{a} {b}"

print (add(1,2))

def format_name(fname, lname):
    formatf = fname.title()
    formatl = lname.title()
    return f"{formatf} {formatl}"

result = format_name("ShIvU", "PaTil")
print (result)
result = format_name(input("First name : "), input("Last name : "))
print (result)