my_name = 'Zed A.Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = int(180) #lbs
my_eyes = 'blue'
my_teeth = "white"
my_hair = "brown"

print "Let's talk about %r." % my_name
print "He's %r inches tall." % my_height
print "He's %d lbs heavy." % my_weight 
print "Actually that's too heavy."
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %d, and %d I get %d." %( my_age, my_height, my_weight,my_age+my_weight+my_height)


metric_height = my_height * 2.54
metric_weight = my_weight * 0.453592
print "To the rest of the world, %s is %2.2f cm tall." % (my_name, 
	metric_height)
print "And they would say he is %2.4f kg heavy." % metric_weight 

