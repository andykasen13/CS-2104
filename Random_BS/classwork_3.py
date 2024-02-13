# classwork due on february 5 2024
import re
from re import Pattern


# Write a Python program to check that a string contains only a-z, A-Z and 0-9 characters.
def challenge_1(string : str) :
    return len(string) == len(re.findall("[a-z]", string))

print("\n------ Challenge 1 ------")
print(challenge_1("hi"))
print(challenge_1("1fsd"))

# Write a Python program to search some literals strings in a string. 
def challenge_2(string : str) :
    searched_words = ['dog', 'fox', 'horse']
    returned_array = []
    for word in searched_words :
        returned_array += (re.findall(word, string))
    return returned_array

print("\n------ Challenge 2 ------")
print(challenge_2("The quick brown fox jumps over the lazy dog."))

# Write a Python program to find the occurrence and position of the substrings within a string.
def challenge_3(string : str) :
    array = re.finditer('exercises', string)
    returned_string = ""
    for item in array:
        returned_string += ("Found " + 'exercises' + " at " + str(item.span()) + "\n")
    return returned_string


print("\n------ Challenge 3 ------")
print(challenge_3("Python exercises, PHP exercises, C# exercises"))

# Write a Python program to remove the parenthesis area and any leading white spaces before the parenthesis in a string. 
def challenge_4(strings : list) :
    returned_array = []
    for string in strings :
        returned_array.append(re.sub(' \(.com\)', '', string))
    return returned_array

print("\n------ Challenge 4 ------")
print(challenge_4(["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]))

# Write a Python program to replace whitespaces with an underscore.
def challenge_5(string : str):
    return re.sub(' ','_', string)

print("\n------ Challenge 5 ------")
print(challenge_5("Python Exercises"))

# Write a Python program to match if two words from a list of words start with the letter 'P'.
def challenge_6(string : str) :
    a = re.findall(r"\bP", string)
    return len(a) == 2

print("\n------ Challenge 6 ------")
print(challenge_6("Python PHP"))
print(challenge_6("Java JavaScript"))
print(challenge_6("C C++"))

# ignore this i have given up at this point. i tried pretty hard
def challenge_7(string : str):
    a = re.findall(r"\bA", string)
    a.append(re.findall(r"\ba", string))
    a.append(re.findall(r'\be', string))
    a.append(re.findall(r'\bE', string))

    return a

#print("\n------ Challenge 7 ------")
#print(challenge_7("The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."))
