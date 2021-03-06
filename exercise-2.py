"""
Exercise 2
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?
"""
There is a logical error when running the function on the second input list.
We expected to see True, yet the function returned False.
There is no error message.
The error is on line 31-32, where the else clause returns False. 
So we need to figure out why it doesn't return True, even though there is 
a part of the list that meets the True condition.

"""

# PART 2: State Assumptions
#
# State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

"""
ok, so for some reason the second example returns False when it should be True.
But it totally meets the condition!
Is the function logic not able to understand the numbers somehow?
Oh wait, you need to wait until the for loop is completely done before 
returning False.
"""

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
    else:
        return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True