'''
Name: Leah Price
Date: 9/3/2025
'''

import math

def hello(string, num = 0):
    st = "Hello " + string 
    if(num == 0):
        print(st)
    else:
        for i in range(num):
            print(st)

def sumChars(thing):
    sum = 0
    for c in thing:
        sum += ord(c)
    return sum

def isPrime(num):
    prime = True
    n = int(num)
    if n <= 1:
        prime = False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
    return prime

#chat helped me figure out how to wrap around the alphabet
def caesarEncrypt(string, num):
    newstring = ""
    for i in string:
        if(i.isalpha()):
            base = ord('A') if i.isupper() else ord('a')
            shifted = (ord(i) - base + num) % 26 + base
            newstring += chr(shifted)
        else:
            newstring += i
    return newstring

class SwearJar:

    def __init__(self):
        self.said = ""
        self.damn = 0
        self.crap = 0
        self.bloody = 0
        self.bullshit = 0
        self.pissed = 0
        self.shit = 0

    def say(self, string):
        self.said = string
        tempstring = string.lower()
        if "damn" in tempstring:
            self.damn += tempstring.count("damn")
        if "crap" in tempstring:
            self.crap += 1
        if "bloody" in tempstring:
            self.bloody += 1
        if "bullshit" in tempstring:
            self.bullshit += 1
        if "pissed" in tempstring:
            self.pissed += 1
        if "shit" in tempstring:
            self.shit += 1
        

    def reportCard(self):
        print("   Damn: ", self.damn)
        print("   Crap: ", self.crap)
        print("   Bloody: ", self.bloody)
        print("   Bullshit: ", self.bullshit)
        print("   Pissed: ", self.pissed)
        print("   Shit: ", self.shit)
        
        list = ["damn", "crap", "bloody", "bullshit", "pissed", "shit"]
        wordcount = len(self.said.split())
        badwordcount = 0
        for i in list:
            badwordcount += self.said.lower().count(i)
        if wordcount == 0:
            percent = 0
        else:
            percent = (badwordcount/wordcount) * 100
            
        print(f"This sentence was {percent:.2f}% profanity.")

    def soap(self):
        self.damn = 0
        self.crap = 0
        self.bloody = 0
        self.bullshit = 0
        self.pissed = 0
        self.shit = 0
        self.said = ""
    


if __name__ == "__main__":
    
    #------------------------------- HELLO FUNCTION -------------------------------

    print("hello function: \n")
    print("Hello Talaga 1 time.")
    hello("Talaga")
    print()
    print("Hello Cherry 3 times.")
    hello("Cherry", 3)
    print()

    #------------------------------- SUMCHARS FUNCTION -------------------------------

    print("sumChars function: \n")
    print(f'131 = {str(sumChars("131"))}')
    print(f'130 = {str(sumChars("130"))}')
    print(f'65 = {str(sumChars("65"))}')
    print()
    
    #------------------------------- SUMCHARS FUNCTION -------------------------------

    print("isPrime function: \n")

    if isPrime(7):
        print("7 is prime")
    else:
        print("7 is not prime")
    
    if isPrime(6):
        print("6 is prime")
    else:
        print("6 is not prime")

    if isPrime(5):
        print("5 is prime")
    else:
        print("5 is not prime")
   #------------------------------- CAESARENCRYPT FUNCTION -------------------------------
     
    print("caesarEncrypt function: \n")
    print(f"This is the origninal = {caesarEncrypt("This is the orginal.", 3)}")
    print(f"Leah is the best = {caesarEncrypt("Leah is the best", -1)}")
    print(f"Computer Science is fun!!! = {caesarEncrypt("Computer Science is fun!!!", 1)}")
    print(f"ABCdefg = {caesarEncrypt("ABCdefg", 1)}")

    
   #------------------------------- SWEARJAR CLASS -------------------------------

    print("SwearJar class: \n")

    classswears = SwearJar()

    string = "Damn, this is fun."
    print(string)
    classswears.say(string)
    classswears.reportCard()
    print()

    print("Using soap!")
    classswears.soap()
    classswears.reportCard()
    print()

    string = "The icecream in this damn town is bloody Shit."
    print(string)
    classswears.say(string)
    classswears.reportCard()
    print()

    

    
