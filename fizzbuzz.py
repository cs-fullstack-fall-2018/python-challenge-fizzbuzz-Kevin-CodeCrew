# Python-Challenge-Loops-FIZZBUZZ
# FIZZBUZZ Milestone challenge
#
# FIZZBUZZ is the classic Programmer's challenge often used as part of job interviews.
#
# User inputs the ending value (e.g. 100) Create a new file called 'fizzbuzz.txt'
#
# Your code should start at 1 and then iterate each number up to the maximum
# If the current number is evenly divisible by 3 you should print "FIZZ" and the number
# If the current number is evenly divisible by 5 you should print "BUZZ" and the number
# If the current number is evenly divisible by both 3 and 5 you should print "FIZZBUZZ" and the number BOTH to the screen and to the file 'fizzbuzz.txt'
# Otherwise, just print the number

import os

os.system("clear")

my_file = open('fizzbuzz.txt', 'w+')

kount = int(input("Enter number of times to run: "))

for num in range(1, kount):
    if num % 3 == 0 and num % 5 == 0:
        out_str = str(num) + " FIZZBUZZ"
        print(out_str)
        my_file.write(out_str + "\n")
    elif num % 3 == 0:
        print(str(num) + " FIZZ")
    elif num % 5 == 0:
        print(str(num) + " BUZZ")
    else:
        print(num)

my_file.seek(0)
print(my_file.readlines())
