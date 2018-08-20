import sys
import os

def main():
    # print (os.getcwd())
    # print (sys.path[0])
    # print (sys.argv[0])
    myjob="hacker"
    for c in myjob[::-1]: print(c)
    for c in myjob: print(c)

    # for c in sys.argv[0][::-1]:
    #     print c + ": " + str(ord(c))
    # b = "12345678"
    # i = 0
    # j=0
    # for c in b[::-1]:
    #     print c
    #     i = i+ int(c)*2**j
    #     j=j+1
    # print i
    # print sys.version
    # s='spam'
    # l=list(s)
    # print l
    # s='%%'.join(l)
    # print s
    # line='bob,hack,46'
    # l=line.split(',')
    # print l

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
