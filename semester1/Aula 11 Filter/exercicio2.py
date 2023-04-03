def testCousin(num):
    primo = True

    for x in range(num-1,1,-1):
        if(num % x == 0):
            primo = False
        
    return primo

p = list(filter(lambda x: testCousin(x) == True, range(1,51)))
print(p)