lst = list[1,2,2,23,3,3]
print(lst)
#homogeniuos,duplication allowed, mutable
lst1 = ["kdjk","jlkd","hsfjh"]
print(lst1)
#determining the list length
#print(lst)
#lst.append(900)
#print(lst)

#l2 = ["Urvesh", "Umang"]
#lst.extend(l2)
#print(lst)
#insert method
lst1.insert(2,8989)
print(lst1)

#remove method
lst1.remove(8989)
print(lst1)

#pop method
#remove top values or latest added value or last value
print(lst1.pop())
print(lst1.pop(1))
print(lst1)

#clear method
print(lst1.clear())
print(lst1)

#list index
list3 = [1,2,3,4,5,6,3,3,3,6,7]
print(list3.index(6))
print(list3.index(3,5,8)) #searches between 5 ro 8  only
#print(list3.index(94)) throws error cause value is not present in the list

#count method +. frequency of the element
print(list3.count(3))

#Copying list
l2 = list3.copy()
list3.insert(0,898998)
print(l2)
#print(list3)

#sort and reversing
list3.sort(reverse = True)
list3.reverse()
print(list3)

l12 = [99,535,535,53,54]
l13 = [9839,7832,383928,9]
l12=l13
l14 = []
#l12 = l13 does not copy l13 into l12

#list comperehencing
#for i in l12:
#    if i % 2 == 0:
#        l14.append(i)

#print(l14)

#Comprehension => while perfomring task the list element is craeted
l45 = [898,483899,32892,93]
odd = [ i for i in l45 if i % 2 != 0]

print(odd)
mb = [ x for x in range(1,7327733288)]
print(mb)
for i in l12:
    if i % 2 == 0:
        l14.append(i)
print(l14)

#matrix 2*2
matrix = [[[2,3][4,5]]][[6,7][8,9]]
print(matrix)