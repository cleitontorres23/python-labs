def speed(space, time):
    s = space/time
    print("Speed: {} m/s".format(s))
    return s

speed(300,1000)
print("################################################################################")

def database(name, age=None):
    if (age is not None):
        return (print("Name is: {} and your age is: {}".format(name, age)))
    else:
        return (print("Age is: {} do not informed".format(None)))


database("Cleiton", 29)
print("################################################################################")

def calc(x,y):
    return {'sum: ': x+y, 'sub: ': x-y }

result = calc(344,102)
for i in result:
    print('{}: {}'.format(i, result[i]))


print("################################################################################")

