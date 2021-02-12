class Animal:

    def __init__(self, kind, color):
        self.kind = kind
        self.color = color 

    def description(self):
        return f'This is a {self.kind}, and this is a {self.color}'
    
cat = Animal('cat', 'orange')
dog = Animal('dog', 'brown')

print(cat.kind)
