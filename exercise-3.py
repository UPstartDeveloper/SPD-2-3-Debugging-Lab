"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

"""
Here is the error message we got from the stack trace:

Traceback (most recent call last):
  File "exercise-3.py", line 34, in <module>
    answer = insertion_sort([5, 2, 3, 1, 6])
  File "exercise-3.py", line 26, in insertion_sort
    while key < arr[j] : 
IndexError: list index out of range

We expect a sorted list but instead there is an IndexError on line 26, 
in the while loop condition. So we need to figure out what causes j to 
go beyond the bounds of the array.


"""


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while j > -1 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

