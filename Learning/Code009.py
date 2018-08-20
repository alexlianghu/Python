import sys
import os

def main():
    # # strFolder = os.getcwd()
    # # strFile=strFolder + "/sample.txt"
    strFile="/Users/alexliang/Documents/sample.txt"
    myFile=open(strFile,'w')
    myFile.write('hello world\n')
    myFile.write('good bye world\n')
    myFile.close()

    myFile=open(strFile)
    L=myFile.readlines()
    myFile.close()
    print (L)


    myFile=open(strFile)
    for line in myFile:
        print (line, end ="")

    myFile.close()

    myFile=open(strFile,'rb')
    for line in myFile:
        print (line, end ="")

    myFile.close()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
