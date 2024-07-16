## Simple Python program to count number of words in sentence

test_string = "Feeling great to complete my second python project. Thanks to MotionCut"

#original string
print ("The original string is : " + test_string)


# using split() function
res = len(test_string.split())

# total no of words
print ("The number of words in string are : " + str(res))