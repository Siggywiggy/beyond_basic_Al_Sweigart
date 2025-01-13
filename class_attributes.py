class CreateCounter:
    count = 0  # This is a class attribute. Keeps count on how many Createcounter objects have been created
    # all Createcounter objects share this attribute!
    def __init__(self):
        CreateCounter.count += 1

print('Objects created:', CreateCounter.count)
a = CreateCounter()
b = CreateCounter()
c = CreateCounter()
print('Objects created:', CreateCounter.count)