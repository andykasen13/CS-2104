"""
@date: 9 February 2024
@author: Andy Garcha
@PID: 906620287
@assignment: Homework 4: Algorithms
@note: Do NOT alter the function headers that are well documented, 
Do put your hw answers in the spaces provided within function headers
"""


def log_base_2(number: float) -> str:
    """ Gives the approximate log base 2 calculation of the input number
    @param number: float to calculate on
    @precondition: number is > 0
    @return str: A string description of the approximate result
    parts i-iii from HW
    
    i. Work out the steps to figure out the 2 concrete examples of 256 and 81
     step by step and briefly explain your work and thinking(5pts)

	ii. Find and describe a pattern and attempt to generalize (5pts)

	iii. Investigate and explain special cases to see if the pattern holds up (5pts)
    """
    if number == 2: return 1
    elif number < 2: return 0.1
    else : return 1 + log_base_2(number / 2)

print("------ Question 1 ------\n------ Log Base 2 ------")
print(log_base_2(81))
print(log_base_2(256))

def reverse_list(aList: list) -> list:
    """Gives a list with the elements in reversed order
    @param aList: list input that's going to be reversed
    @return list: the reversed version of the input list
    parts i-iii from HW
    i. Work out the steps to figure out a concrete example and briefly explain
     your work and thinking(5pts)

	ii. Find and describe a pattern and attempt to generalize (5pts)

	iii. Investigate and explain special cases to see if the pattern holds up (5pts)
    """

    if len(aList) <= 1 : return aList
    return [aList[len(aList) - 1]] + reverse_list(aList[1:len(aList) - 1:]) + [aList[0]]
print("\n------ Question 2 ------\n----- Reverse List -----")
print("Expected: [9, 8, 7, 6, 5, 4, 3, 2, 1]\nActual:   " 
      + str(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9])))
print("\nExpected: [3, 2, 1]\nActual:   " 
      + str(reverse_list([1, 2, 3])))
print("\nExpected: [2, 1]\nActual:   " 
      + str(reverse_list([1, 2])))
print("\nExpected: [8, 7, 6, 5, 4, 3, 2, 1]\nActual:   " 
      + str(reverse_list([1, 2, 3, 4, 5, 6, 7, 8])))
