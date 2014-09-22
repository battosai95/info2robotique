#!/usr/bin/python2.7
for i in range(10):
    print "{greetings} nombre {nb}".format(nb=i, greetings='Salut')
    if (i % 2 == 0):
        print "tu es pair"
    else:
        print "tu es impair"
print "fin"
