# import sys
# import os

def main():

    # T=(6,5,4,3,2,1)
    # L=list(T)
    # L.sort()
    # T=tuple(L)
    # print (T)
    #
    # L= [x **2  for x in T]
    # print (tuple(L))
    #
    # T=tuple(L)


    T=(1,[2,3],4)
    T[1][1]='haha'
    print (T)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
