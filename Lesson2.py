
print('**** taple')

table = (1,2,3,4 , '5')

print(table)
print(table[0:2])

print(table[:-1])

print(table[::-1])

print(table[:2])

print('**** can be added more values')
table2 = table + (7,8,9,10,11)
print(table2)

print('**** table List')
tableList = [1,2,3,4 , '9','5']

print(tableList)

print(tableList[1])
tableList[1] = 0
print(tableList)

print('**** pointers')
Lst2 = tableList
print(Lst2 is tableList)
tableList[1] = 3
print(Lst2)

print('**** copy list')
Lst2 = tableList[:]

tableList[1] = 66
print(tableList)
print(Lst2)

print('can be added more values')

Lst2.append(0)
print(Lst2)

Lst2.insert(0,655)
print(Lst2)

#we can use copy,remove,sort

print('****  can be pop elemant using by .pop(0) or pop(-1) LIFO or FIFO')
a =Lst2.pop(0)
print(a)
print(Lst2)

#placing data
tpl3 = 2,5
c,d = tpl3
print('C: ',c,'D: ',d)

#all other elemnts in e
tpl4 = 3,4,6,7
c,d ,*e= tpl4
print('C: ',c,'D: ',d)
print('E: ',e)

print('****  swap values tricks')
c= 9
d=6
print('C: ',c,'D: ',d)
c,d =d,c
print('C: ',c,'D: ',d)

print('****  Dictionary')
dict1 = {'a':'123' ,1 : 22}

print('add element ')
dict1[6] = 54
print(dict1)
print(dict1['a'])
print(dict1[1])

print('****  can be pop ')
res = dict1.pop(1)
print(res)
print(dict1)

print('****  can be update ')
res = dict1.update({ 9: 55, 11:88})
print(dict1)

