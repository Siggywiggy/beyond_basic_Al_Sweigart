class ExampleClass:
    def exampleRegularMethod(self):
        print('This is a regular method')

    @classmethod
    def exampleClassMethod(cls):
        print('This is a class method!')

ExampleClass.exampleClassMethod()

obj = ExampleClass()
obj.exampleClassMethod()
obj.__class__.exampleClassMethod()