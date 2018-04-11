def word_split(words):
	split = words.split(",")
	return split
	
def sort_words(split):
	after_sort =sorted()
	return after_sort	

str = "a,b,c"
# split the sentence separated by comma
after_split = word_split(str)

# sort the returned string list
after_sort = sort_words(after_split)
print after_sort
	

