""" Order Mayus / minus string """

def orderLowerUpper( stringUser ) :
    
    lowerString = ""
    upperString = ""

    for letter in stringUser :
        if letter.islower() :
            lowerString += letter
        else : 
            upperString += letter
        
    return lowerString + upperString

# get user string
stringUser = input("Introduce un string a ordernar: ")

# invoque function
print( orderLowerUpper(stringUser) )