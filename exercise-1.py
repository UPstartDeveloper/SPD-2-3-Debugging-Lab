"""
Exercise 1
"""

# PART 1: Gather Information
#
# Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?
"""
Here is the stack trace we got from the running program:
# Traceback (most recent call last):
#   File "exercise-1.py", line 31, in <module>
#     answer = find_largest_diff([5, 3, 1, 2, 6, 4])
#   File "exercise-1.py", line 23, in find_largest_diff
#     diff = abs(list_of_nums[i] - list_of_nums[i+1])
# IndexError: list index out of range

There is an IndexError on line 31 because on the last iteration of the for loop 
because we index outside the bounds of the list_of_nums. We expected to find just
the largest difference between consecutive numbers. This means we need to find out 
why i has a value that's greater than or equal to the length of the list.
"""


# PART 2: State Assumptions
#
# State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

"""
"hmm, so why is it i or i + 1 going out of bounds?
oh, I see. We should set the for loop to go 1 less than the length of 
the array, because then i will then stop at len(list_of_nums) - 2, 
and therefore i + 1 will stay within the array bounds."
"""

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums) - 1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)