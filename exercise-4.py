"""
Exercise 4
"""

# PART 1: Gather Information
#
# Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

"""
Here is the error message from the stack trace:
  File "exercise-4.py", line 22
    if high == None:
                   ^
IndentationError: unindent does not match any outer indentation level

We expected to return the index at which a given element is in an array, however 
there is an IndentationError on line 22, where we check whether high is None.
So we need to figure out which column we should actually start this line 
(or some line above it) in the function body.

"""


# PART 2: State Assumptions
#
# State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

"""
Hmm, so why isn't it working?
The logic is fairly accurate - if the value at the middle is too smaller, 
go right;
and when it's larger, go left.

Maybe we need hit the base case?
Hmm, maybe print out the values of low, mid, and high?
Oh I see! So we assumed that high < low eventually, 
or we find the element.

However, we forgot to consider that we're including elements that have already
been checked when we recurse - so we need to increment/decrement the middle 
index when we call the function recursively. 
"""

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid - 1)

    else: 
        return binary_search(arr, element, mid + 1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)