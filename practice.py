mainDataTypes = ['strings','numbers','lists','tuples','dictionaries/maps']

#lists: how to print an item in a list. Lists are arrays
print mainDataTypes
print mainDataTypes[0]
print mainDataTypes[0:]

#now to change a value of a list item example:
# mainDataTypes[0] = 'new value'

#lists inside of lists. Basically boxes inside of boxes
anotherList = ['school','work','friends','sleep']
someMore = ['sushi','burgers','pasta']

everythingNow = [anotherList, someMore]
print everythingNow

someMore.append('pancakes')
someMore.instert(3,'noodles')
someMore.remove('noodles')

#tuples. we won't be able to change a tuple after it is created.


