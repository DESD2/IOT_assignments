# Write a function find_longest_word() that takes a list of words and 
# returns the length of the longest
# one.

def max_len(list):
    max = len(list[0])
    max1 = list[0]
    for x in list:
        if( len(x) > max):
            max = len(x)
            max1 = x
    print (f"longest word is ",max1)
    print (f"length of word is ",max)


a=["one","three","two","shreyas"]

max_len(a)