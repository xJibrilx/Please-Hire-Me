import random
import itertools
value = random.random()
i = value
def resurrection():
    print("Jesus Is Lord") # yes he is
def value():
    return random.uniform(0,1)# random selection between 0 and 1
while i != 1: # dice roll of the code
    for x in itertools.count():  # the counter function +1 increment
        print(value())
        print(x)
        if (value()) >= 1:# important to note when dealing with decimals to use or equals
            (resurrection())
            break
    else:
        continue # only executed if the inner loop did NOT break
    break # only executed if the inner loop DID break
# How long before Jesus resurrects
