# tuple :-
#        1) syntax= ()
#        2) value does not be changed ,its fixed
#        3) order form
#        4) tuple accept duplicate element
#        5) allow only same to add()

############################# ex:-
#tup=(1,2,3.2.1.2.'niraj') 
#print(type(tup))      

######################## for single element
#tup=(1,)
#print(type(tup))

tup=(1,2,3,4,5,)

############################ (for change list to tuple or tuple to list)

#lst=list(tup)
#lst[2]=5
#print(lst)
#tup=tuple(lst)
#print(tup)

############################ duplicate
#tup=(1,1,1,2,2,2)
#print(tup)

############################ for acces

#single:-
#print(tup[1])

#multiple:-
#print(tup[1:4])      # ( n - 1)

################################# add

#tup1=(6,7,8)
#tup2=(4,5,2)
#tup1=tup1+tup2
#print(tup1)

##############################  len

#print(len(tup))

##############################

tup=(1,2,3,4,5)

lst=list(tup)
#lst[4]=10
#print(lst)

#lst.append(6)
#print(lst)

lst.insert(5,6)
print(lst)

#tup=tuple(lst)
#print(tup)


