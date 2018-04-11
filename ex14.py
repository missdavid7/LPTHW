from sys import argv 

script, user_name = argv 
prompt = '>'

print "Hi %s, I am the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
#print "Do you like me %s?" % user_name
likes = raw_input ("Do you like me?\n")

#print "Where do you live %s?" % user_name
lives = raw_input ("Where do you live\n")

#print "What kind of computer do you have?"
computer = raw_input ("What kind of computer do you have\n")

print """
Alright, so you said %s about liking me. 
You live in %s. Not sure where that is. 
And you have a %s computer, nice.
""" % (likes, lives, computer)
