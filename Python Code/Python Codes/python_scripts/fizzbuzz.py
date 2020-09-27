for x in range(1,101):
    if x % 5 == 0 and x % 3 == 0:
        print x, "FizzBuzz"
    elif x % 5 == 0:
        print x, "Buzz"
    elif x % 3 == 0:
        print x, "Fizz"
    else:
        print x
        

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')

print(tuple1 + tuple2)

import math
print ('The value fo pi is %5.3f' % math.pi)
