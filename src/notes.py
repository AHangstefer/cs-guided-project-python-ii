class Animal:

    def __init__(self, kind, color):
        self.kind = kind
        self.color = color 

    def description(self):
        return f'This is a {self.kind}, and this is a {self.color}'
    
cat = Animal('cat', 'orange')
dog = Animal('dog', 'brown')

print(cat.kind)


#ACCESSING ITEMS IN list

my_list = [1,3,2,4,5,6]

print(my_list[4])
#this gets the last element
print(my_list[-1])
#this gets the 3rd last element
print(my_list[-3])
#this gets the beginning
print(my_list[-0])

#Getting subarrays
#get first 3 elements
print(my_list[0:3])
print(my_list[4:])
print(my_list[:7])
