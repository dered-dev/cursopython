""" Filter unique items in a list function """

# set solution
def setList( listUser ) :
    return list( set( listUser ) )

print( setList( [1,2,3,3,2] ) )

# for solution
def setListFor( listUser ) :
    uniqueList = []
    for item in listUser :
        if item not in uniqueList :
            uniqueList.append(item)
    
    return uniqueList


print( setListFor( [1,1,3,3,2,9,3,5] ) )
