# Find and return pi to Nth number of decimals. Keep a limit to how far the programme will go.


def gregory_leibniz():
    """ Gregory-Leibniz Series:
        pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
        if you continue this pattern forever you will be able to calculate pi/4 exactly and then just
        multiply it by 4"""
    negative = True
    pi = 1
    myList = [x for x in range(3,99999999) if x%2]
    for i in myList:
        if negative:
            pi -= (1/i)
            negative = False
        else:
            pi += (1/i)
            negative = True

    return pi*4

def start():
    print (gregory_leibniz())

if __name__ == '__main__':
    start()