#DYLAN BOUDREAU#

import array
import random

def temp_dev(temps):
    n = len(temps)
    mean = sum(temps) / n
    var = sum((x - mean)**2 for x in temps) / n
    dev = var ** 0.5
    if dev <= 1.0:
        print("COMFY")
    else:
        print("NOT COMFY")

temps = array.array("f")
for items in range(0,10):
    temps.append(random.uniform(68, 80))

print(temps[0],"",temps[1],"",temps[2],"",temps[3],"",temps[4],"",temps[5],"",temps[6],"",temps[7],"",temps[8],"",temps[9])
temp_dev(temps)
