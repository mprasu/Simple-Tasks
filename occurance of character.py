#program to count the number occurrence of a specific character in a string
a=input("enter the string")
b=input("enter ur character")
print(a.count(b))
#or
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
str1=input("enter ur value")
print(char_frequency(str1))
#word count
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
str=input("enter ur value")
print( word_count(str))
