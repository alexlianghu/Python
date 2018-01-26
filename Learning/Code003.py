"""
names=["Alex", "HU", "Cherry", "Li", "Annie"]
for word in names:
	if word[0] in "HL":
	    print ("Hello " + word)
"""


# names=["Alex", "HU", "Cherry", "Li", "Annie"]
# hilightName=[]
#
# for name in names:
#     if name[0] in "HL":
#         hilightName.append(name)
#
#
# print hilightName

prices=[1.5,11.9,20.5,11.5,19.5]
total=0
for price in prices:
    total=total+price

print "Total = " + str(total)
print "Sum(prices) = " + str(sum(prices))
