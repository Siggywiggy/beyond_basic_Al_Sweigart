import time, cProfile, rsaCipher
import timeit


def addUpNumbers():
    total = 0
    for i in range(1, 1000001):
        total += i


cProfile.run("addUpNumbers()")
cProfile.run(
    "rsaCipher.encryptAndWriteToFile('encrypted_file.txt', 'al_sweigart_pubkey.txt', 'abc'*100000)"
)


def hashset_2_sum():
    numbers = [2, 7, 11, 15, 6, 98, 75, 3, 4, 87, 1, 8, 5]
    target = 9

    seen_dict = dict()

    for i, num in enumerate(numbers):
        # add the number and its index to the dictionary
        seen_dict[num] = i
        diff = target - num
        if diff in seen_dict.keys():
            return (seen_dict[diff], i)
        else:
            continue


cProfile.run("hashset_2_sum()")
print(timeit.timeit("hashset_2_sum()", globals=globals()))
