from audioop import reverse
import collections
from typing import Counter

def hw():

    x = 1
    while x > 0:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))

        try:
            print(a/b)
            print("Out of try except blocks")

        except ZeroDivisionError:
            print("Divison by zero not allowed")
            print("Out of try except blocks")
            break





if __name__ == "__main__":
        hw()

