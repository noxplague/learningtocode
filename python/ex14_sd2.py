from sys import argv

script, user_name, hal = argv
prompt = '> '

print "Hi %s, I'm the %s script.  I'm known as %s" % (user_name, script, hal)
print "I'd like to ask you a few questions."
print "Do you like %s, %s?" % (hal, user_name)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so your said %r about liking %r.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
""" % (likes, hal, lives, computer)