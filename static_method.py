class ExampleClassWithStaticMethod:
    # static methods cant access attributes or methods of the class or its objects
    @staticmethod
    def sayHello():
        print('Hello!')

# Note that no object is created, the class name precedes sayHello():
ExampleClassWithStaticMethod.sayHello()