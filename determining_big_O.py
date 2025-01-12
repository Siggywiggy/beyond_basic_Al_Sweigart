def readingList(books):
    print('Here are the books I will read:')  # 1 step
    numberOfBooks = 0                         # 1 step
    for book in books:                        # n * 2 steps in the loop
        print(book)                           # 1 step # already counted
        numberOfBooks += 1                    # 1 step # already counted
    print(numberOfBooks, 'books total.')      # 1 step

# 2n + 3 => n => O(n) linear time

def quadraticExample(someData):  # n is the size of someData
    for i in someData:           # n steps
        for j in someData:       # n steps
            print('Something')   # 1 step
            print('Something')   # 1 step
            print('Something')   # 1 step

# n * n * n + 3n => n^3 + 3n => polynomial time

def count_book_points(books): # books = n
    points = 0                # 1 step
    for book in books:        # n * steps in loop
        points += 1           # 1 step

    for book in books:          # n * steps in loop
        if 'by Al Sweigart' in book: # 1 step
            points += 1         # 1 step

    return points               # 1 step

# 5 + n + n => 5 + n*1 + n*2 => O(n) => linear time

def iLoveBooks(books):
    for i in range(10):              # 10 * steps in the loop
       print('I LOVE BOOKS!!!')     # 1 step
       print('BOOKS ARE GREAT!!!')  # 1 step

# 10 + 1 + 1 = 12 => O(1) => constant time

def cheerForFavoriteBook(books, favorite):
    for book in books:                              # n * steps in loop
        print(book)                                 # 1 step
        if book == favorite:                        # 1 step
            for i in range(100):                    # 100 steps
            print('THIS IS A GREAT BOOK!!!')        # 1 step

# 103 + n => O(n) => linear time

def findDuplicateBooks(books):
    for i in range(books):                          # n * steps in loop
        for j in range(i + 1, books):               # n * steps in loop
            if books[i] == books[j]:                # 1 step
                print('Duplicate:', books[i])       # 1 step

# n * n + 2 => n^2 + 2 => polynomial time


def binarySearch(needle, haystack):
    if not len(haystack):                           # 1 step
        return None                                 # 1 step
    startIndex = 0                                  # 1 step
    endIndex = len(haystack) - 1                    # 1 step

    haystack.sort()                                 # n * log^2 n
    while start <= end:                             # log^2 n
        midIndex = (startIndex + endIndex) // 2     # 1 step
        if haystack[midIndex] == needle:            # 1 step
            # Found the needle.
            return midIndex                         # 1 step
        elif needle < haystack[midIndex]:           # 1 step
            # Search the previous half.
            endIndex = midIndex - 1                 # 1 step
        elif needle > haystack[mid]:                # 1 step
            # Search the latter half.
            startIndex = midIndex + 1               # 1 step

# .sort() is higher order n * log n over log n => the whole function is n * log n