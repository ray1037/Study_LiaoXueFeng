# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
#用len()函数可以获得list元素的个数：
print(len(classmates))
#用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
print(classmates)
#可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print(classmates)
#删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
#删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)
#把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)

