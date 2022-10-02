from audioop import reverse
import collections
from typing import Counter

def hw():

    print("Adja meg a háromszög oldalát cm-ben: ")
    aold = int(input("a oldal (cm): "))
    bold = int(input("b oldal (cm): "))
    cold = int(input("c oldal (cm): "))

    if (aold + bold > cold) and (aold + cold > bold) and (bold + cold > aold):
        print("A", aold, bold, "és", cold, " oldalú háromszög szerkeszthető.")
    else:
        print("A", aold, bold, "és", cold, " oldalú háromszög NEM szerkeszthető.")

if __name__ == "__main__":
        hw()

