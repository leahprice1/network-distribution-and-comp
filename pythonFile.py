"""
pythonFile.py
--
Name: Leah Price
Sept 2, 2025
Desc: Solution to Python Problem Set 1

"""
import math
import string

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

  print("\nhello-function")
  print("\nHello Bob 1 time")
  hello("Bob")

  print("\nHello Bill 5 times")
  hello("Bill", 5)

  print("\nsumChars")
  print("65 = {}".format(sumChars("A")))
  print("130 = {}".format(sumChars("AA")))
  print("131 = {}".format(sumChars("AB")))
  print("131 = {}".format(sumChars("BA")))

  print("\nisPrime")
  print("True = {}".format(isPrime(7)))
  print("True = {}".format(isPrime(2)))
  print("False = {}".format(isPrime(6)))

  print("\ncaesarEncrypt")
  print("bcdea = {}".format(caesarEncrypt("abcdz", 1)))
  print("BCDEA = {}".format(caesarEncrypt("ABCDZ", 1)))
  print("bc?de. = {}".format(caesarEncrypt("ab?cd.", 1)))
  print("abcd = {}".format(caesarEncrypt("efgh", -4)))

  print("\nNo words given, should be all 0's.")
  sw = SwearJar()
  sw.reportCard()

  print("\nThis is a damn sentence.")
  sw = SwearJar()
  sw.say("This is a damn sentence.")
  sw.reportCard()
  sw.soap()
  print("\nSoap() called\n")
  print("This shITty homework will be the end of me.")
  print("The icecream in this damn town is bloody Shit.")
  sw.say("This shITty homework will be the end of me.")
  sw.say("The icecream in this damn town is bloody Shit.")
  sw.reportCard()

  print("\nNo words given, should be all 0's.")
  sw = SwearJar()
  sw.say("This damn assignment is bloddy bullshit.")
  sw.say("Python is a craptastic language that makes me pissed")
  sw.say("to program.")

    

    
