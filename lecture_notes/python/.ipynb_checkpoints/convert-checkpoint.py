def ftoc(temp):  # *F to *C
    return (temp-32.0) * (5.0/9.0)
    
def ctof(temp):  # *C to *F
    return temp * (9.0/5.0) + 32.0
    
def convert(temp, toTemp):  # Two parameters
    # No problem to call another function in the body of a function
    if toTemp.lower() == "c":
        return ftoc(temp)  # function call to ftoc
    else:
        return ctof(temp)  # function call to ctof



print('convert.py')
print(convert(23,'c'))

