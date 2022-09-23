from audioop import reverse
import collections
from typing import Counter


def hw1():
    be = str(input("Adjon meg egy mondatot: "))
    
    counter = collections.Counter(be)
    
    print(dict(counter))
    
    reverse = (be[::-1])
    
    print(reverse)
    
    words = be.split()
    thislist = [words]
    print(thislist)
    
    
def hw2():
    beszam = int(input("Adjon meg egy számot és egy mértékegységet (cm/inch):\n")) 
    bemertek = str(input())  
    valtozo = 2.54 
    if bemertek == "cm":     
            print(beszam / valtozo, "inch") 
    elif bemertek == "inch":     
            print(beszam * valtozo, "cm" ) 
    else:     
            print("Not correct unit!")
    
if __name__ == "__main__":
    hw1()
    hw2()
