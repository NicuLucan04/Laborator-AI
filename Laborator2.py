'''#my_list=[1,2,'Robert', 'Hanea']
#print(len(my_list))
#print(my_list.index(2))
#print(my_list.count('Hanea'))
#print(my_list[2])
#print(my_list[1:])
#print(my_list[-2])
#print(my_list*2)
#print(my_list+[100])
#print(my_list.append(100))
#print(my_list.extend([100,50]))
#listanumerodos=['castraveti','par','portocale']
#new_listanumerodos=listanumerodos.copy()
#new_listanumerotres=listanumerodos[:]
#print([1,2,3].pop())
#print([1,2,3].pop(1))
#print([1,2,3].remove(2))
#print([1,2,3].clear())
#del [1,2,3][0]
print([1,2,5,4,3].sort())
print([1,2,5,4,3].sort(reverse=True))
print(sorted([1,2,5,4,3]))
list(reversed([1,2,5,4,3]))
1 in[1,2,5,4,3]
print(min([1,2,5,4,3]))
print(max([1,2,5,4,3]))
mList=[22,25,44,45,75,84,63,49,485,55]
first,*x,last=mList
print(first)
print(last)'''
'''my_dict={'nume':'Nicolae Lucan','varsta':21,'puncte_tari':False}
print(my_dict['nume'])
print(len(my_dict))
print(list(my_dict.keys()))
my_dict['mancare_preferata']='Ovaz cu proteina, banane, afine '
print(my_dict.get('varsta'))
del.my_dict['nume']
'''
my_set=set()
my_set.add(1)
my_set.add(100)
my_set.add(10)
new_list=[1,5,4,6,67,5,21,12,3]
set(new_list)
print(my_set.remove(100))
print(my_set.discard(100))
my_set.clear()
new_set={1,2,3}.copy()
set1={5,7,8}
set2={10,11,12}
set3=set1.union(set2)
set4=set1.intersection(set2)
