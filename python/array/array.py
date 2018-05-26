import numpy as np 

'''
a = np.array([1, 2, 3, 4])
b = np.array((1, 2, 3, 4))

print 'a is :', a
print 'b is :', b

# what is the difference between list and tuple?

#Read data from string and store them into an array
#This will be useful when I am going to read MTG data from .mtg file
test_string1 = '1 2 3 4 5'
array = np.fromstring(test_string1, dtype = int, sep=' ')
print array
'''

'''
#Fill the array 
print np.ones((3, 4))
print np.zeros((3, 4), int)
print np.zeros((3), int)
print np.empty((3, 4))
print np.full((3, 4), 100)
'''

EEC1 = "(1 1*2)(2 3)(4 5-6)"
EEC2 = "(1 1*2)"
EEC_data = []
EEC_symble = []


#list.append, list.extend, list.insert

def seperate_EEC(eec):
    for i, ch in enumerate(eec):
        if ch.isdigit():
            EEC_data.append(ch)
        elif ch.isspace():
            EEC_symble.append('\/')
        else:
            EEC_symble.append(ch)

seperate_EEC(EEC1)

print EEC_data    
print EEC_symble

'''
a1 = [1, 2, 3]
a2 = [4, 5, 6]
a = []

a.append(a1)
a.append(a2)
print a

'''

a = ['a',' b', 'c', 'a', 'd', 'e', 'a']


i = 0
while i < len(a):
    if a[i] == 'a':
        a.pop(i)
        i -= 1
    else:
        print a[i]
    i += 1
#print a

#Can't copy list like this!!
tmp = a
for i in range(len(tmp)):
    if a[i] == 'a':
        a.pop(i)
#print a

arr1 = ['a', 'b']
arr2 = ['b', 'a', 'a']

arr3 = "ab"
arr4 = "abc"

result = arr1 in arr2
result = arr3 in arr4


def sub_match(list1, list2):
    if len(list1) > len(list2):
        return False

    for i in range(len(list1)):
        for j in range(len(list2)):
            if (list2[j] == list1[i]):
                break
            if (j == len(list2)-1 and list2[j] != list1[i]):
                return False
    return True
            

result = sub_match(arr1, arr2)
print result
        


