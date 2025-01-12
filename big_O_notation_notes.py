"""

    O(1), Constant Time (the lowest order) - look if bookshelf is empty -
    regardless of bookshelf size same amout of work

    O(log n), Logarithmic Time - look for a book in sorted bookshelf - binary search algo
    where we keep splitting the books in half (log 2 n). The amount of books can double but the runtime only increases by 1 step
    divide and conquer

    O(n), Linear Time - read books - twice the books twice the time spent on reading

    O(n log n), N-Log-N Time - sorting the books - O(n) * O(log n) - O(log n) to find a books place via binary search * n books

    O(n2), Polynomial Time - check for duplicate books on unsorted bookshelf - start with first book and compare with every
    one of the other books. We have to check n * n times! n(quared) - runtime increases by the times books increase SQUARED
    
    O(2n), Exponential Time - evey possible combinaton of books  - each additional book doubles the workload - 2 books - 4 combinations
    3 books - 8 combinations

    O(n!), Factorial Time (the highest order) - every possible order of books - permutations. 3 books - 6 permutations.
    Traveling salesman conundrum

    Big O - measures worst case scenario

    big Omega - best cast scenario

    big Theta - algorithms that have the same best and worst case


"""