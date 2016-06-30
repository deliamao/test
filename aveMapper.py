import sys
SOH ='\x09'
for line in sys.stdin:
    data = line.strip('\n').split(SOH)
    if len(data) ==2:
        user, itemCat = data
        print "{0}\t{1}".format(1,itemCat)


