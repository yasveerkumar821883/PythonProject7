l1=["yash",243,"India","Ayodhya"]
l1.append("RAM")#add element end off the list
l2=[24,53]
# l1.extend(l2)#add list end of list
# l1.insert(2,"rohan")
new_l1=l1.copy()
ind=l1.index("yash")
print("return append list : ",l1)
print("return extend list : ",l1)
print("return inserted list : ",l1)
print("print the copy of list 1 : ",new_l1)
print('print the index of \"Yash\"',ind)
l3=[1,23,34,54564,3,765,8,86,86,433,5,6]
l3.sort()# this method sort the list
print("Sorted list : ",l3)
l3.reverse()# this method will reverse the list
print("Reverse list : ",l3)