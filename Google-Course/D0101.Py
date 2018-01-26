
#!
#cd ~/Dropbox/Personal/Learning/Python-Google

import sys


def Hello(name):
	if (name == 'Alex') :
		name = name + ' i \'knew\' it !!!!'
		print 'Hello' + name
	name = name + ' i like it !!!!'
	print 'Hello', name.upper()
	
	
#define a main() function that prints a little greeting
def main():
	Hello(sys.argv[1])
	print sys.argv[0]
	print sys.path[0]


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__' :
	main()