# # This prints out "John is 23 years old."



# name = "John"
# age = 23
# print("%s is %d years old." % (name, age))

# # This prints out: A list: [1, 2, 3]
#
# mylist = [1,2,3]
# print("A list: %s" % mylist)

# This prints out: A list: [1, 2, 3]
# mylist = [1,2,3]
# print("A list: %s" % mylist)

# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s. Your current balance is $%s"
#
# print(format_string % data)


# astring = "Hello world!"
# print(astring.index("o"))
#
# print(astring.count("o"))
#
# print(astring[3:7:3])
#
# print(astring[::-1])
#
# print(astring[::1])

# import re
# match = re.match('/(.*)/(.*)/(.*)','/usr/home/disk')
# print match.groups()
#
# L=[123,'spam',1.24]
# L.append(18)
# print (L)
# # print (len(L))
# # print (L[:-1])
# # print (L[1:-1])
# # print (L[2])
# # L.pop(2)
# #L.remove(1.24)
# L.insert(2,'shanghai')
# L.sort()
# L.reverse()
# print (L)
# print (L[-2])

# M = [[1,2,3],[4,5,6],[7,8,9]]
# print (M)
#
# col2 = [row[0] for row in M]
# print (col2)
# col2 = [row[0]*10 for row in M if row[0] % 2 !=0]
# print (col2)

# col2 = [M[i][j] for i in [0,1] for j in [1,2] ]
# print (col2)

# doubles = [c * 2 for c in '1234']
# print doubles

# G = (sum(row) for row in M)
# print next(G)
# print next(G)
# print next(G)

# print list(map(sum,M))

# D = {'food': 'chicken','quantity' : 15, 'color': 'pink'}
# D['expiration'] = '2018-09-01'
# print D
# D['quantity'] +=1
# print D

# rec = {'name':{'first':'Alex','last':'Liang'}, 'title':['director','product'],'age':44}
# # print rec['name']['last'] + ' ' + rec['name']['first'] + ' IS '+ str(rec['age']) + ' Years Old'
# # print rec['name']['last'] + ' ' + rec['name']['first'] + ' IS '+ rec['title'][1]
# print rec
# Ks=list(rec.keys())
# print Ks
# Ks.sort()
# Ks.reverse()
# print Ks
# for key in Ks:
#     print key + ' : ' + str(rec[key])

# for c in 'shanghai':
#     print c.upper()
#
# x=5
# while x>0:
#     print ('shanghai' * x)
#     x-=1

# squ = [x **2 for x in [11,12,13,14,15,16,17,18,19]]
# print squ

# squ ={}
# x = 10
# squ['10'] = 100
# while x<20:
#     squ[str(x)] = x**2
#     x +=1
#
# print squ
#
# for key in sorted(squ):
#     print (key + "**2  = " + str(squ[key]))
#
# f = open('test123.txt','w')
# f.write('Hello\n')
# f.write('2010\n')
# f.close()
#
# f = open('test123.txt')
# test = f.read()
# print test
# x = test.split()
# print x
# print type(x)

# x=21
# M={}
# while x<30:
#     # print str(x**2)
#     M[str(x)]=x**2
#     x +=1
# print M
# for key in sorted(M):
#     print (key + "**2  = " + str(M[key]))