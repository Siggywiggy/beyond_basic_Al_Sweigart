# Regular class attribute

class ClassWithRegularAttributes:
    def __init__(self, someParameter):
        self.someAttribute = someParameter

obj = ClassWithRegularAttributes('some initial value')
print(obj.someAttribute)  # Prints 'some initial value'
obj.someAttribute = 'changed value'
print(obj.someAttribute)  # Prints 'changed value'
del obj.someAttribute  # Deletes the someAttribute attribute.

class ClassWithProperties:
    def __init__(self, someParameter):
        self.someAttribute = someParameter

    @property
    def someAttribute(self): # getter method
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value): # setter method
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self): # deleter method
        del self._someAttribute

obj = ClassWithProperties('some initial value')
print(obj.someAttribute) # Prints 'some initial value'
obj.someAttribute = 'changed value'
print(obj.someAttribute) # Prints 'changed value'
del obj.someAttribute # Deletes the _someAttribute attribute.

