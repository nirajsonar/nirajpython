# #########   set:-
# 1) set unordered
# 2) does not store repeted value
# 3) unique
# 4) syntax  ={}
# 5) set is unchanged, we can not change,we can remove old ele and add new

#set={1,2,3,4,5}
#print(type(set))

#set={1,1,1,2,2,2}
#print(set)

#set={True,1,2,3,1.2,1.3,'niraj',False}
#print(set)

#set={1,2,3,4}
#print(len(set))

#set={1,2,3}
#set.add((4))
#print(set)

#set1={1,2,3}
#set2={6,4,5}
#set1.update(set2)
#print(set1)

#set={1,2,3,4}
#set.clear()
#print(set)

# #set={1,2,3,4}
# #set.remove(2)
# #print(set)

# #set={1,2,3,4}
# #del lst[1]
# #print(lst)

tup=(1,1,3,5,5,9,8)
set=set(tup)
print(type(set))
set.remove(9)
set.add(10)
tup=tuple(set)
print(tup)


