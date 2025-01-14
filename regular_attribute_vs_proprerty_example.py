# Regular class attribute

class ClassWithRegularAttributes:
    def __init__(self, someParameter):
        self.someAttribute = someParameter

obj = ClassWithRegularAttributes('some initial value')
print(obj.someAttribute)  # Prints 'some initial value'
obj.someAttribute = 'changed value'
print(obj.someAttribute)  # Prints 'changed value'
del obj.someAttribute  # Deletes the someAttribute attribute.

# class proprty example
class ClassWithProperties:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self): # This is the "getter" method.
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value): # This is the "setter" method.
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self): # This is the "deleter" method.
        del self._someAttribute

obj = ClassWithProperties()
print(obj.someAttribute) # Prints 'some initial value'
obj.someAttribute = 'changed value 2'
print(obj.someAttribute) # Prints 'changed value'

del obj.someAttribute # Deletes the _someAttribute attribute.