from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)

out_file = open(to_file, 'w').write(indata)

print "Alright, all done."