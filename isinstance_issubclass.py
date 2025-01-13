class ParentClass:
    pass


class ChildClass(ParentClass):
    pass


parent = ParentClass()
child = ChildClass()

print(isinstance(parent, ParentClass))
print(isinstance(parent, ChildClass))
print(isinstance(child, ChildClass))
print(isinstance(child, ParentClass))

print(isinstance(42, (int, str, bool)))