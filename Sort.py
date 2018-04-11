sort_list = [2,5,3,1,7]
print sorted(sort_list) # Method 1

after_sort = sort_list.sort()
print after_sort # None

sort_list.sort()
print sort_list #Method 2 

# Sort is only used for list! 
# Sort does not return any value but it changes from the original list.
# eg Sort

aList = [123,"xyz","abc","zara"]
aList.sort()
print aList


# Sorted can be used for any iterable
Sentence = "This is a test string form Andrew."
# sorted must used on some iterable
Sort_S = sorted(Sentence)
print (Sort_S)

# Advanced 
Sort_Advanced = sorted(Sentence.split(),key=str.lower)
print (Sort_Advanced)




