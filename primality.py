# Primality test. Execution time O(√n)

import math
import sys

def main():
    while(True):
        # Number to be verified
        x = int(input("X: "))
        # The number must be greater than 1
        if(x < 2):
            main()
        elif(x == 2):
            print("Primo")
            break
        # For x too large change upper limit in range to X and delete variable limit.
        # Because if the whole is too big it cannot be converted into a float. Time execution will change in n
        limit = int(math.sqrt(x))
        for i in range(2, limit):
                if(x%i == 0):
                    print("non primo")
                    sys.exit()
        if(x%(math.sqrt(x)) == 0):
            print("non primo")
        else:
            print("primo")
            sys.exit()
main()
