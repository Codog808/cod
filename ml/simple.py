import random

def main():
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    user = input("Give me something ")
    
    vals = []
    for letter in user:
        vals.append(alphabet.index(letter.lower()))
    
    stringo = []
    for _ in range(0,10):
        for val in vals:
            val = random.randint(1,10) + random.randint(1,10) * val 
            stringo.append(alphabet[val % 27])
        print("".join(stringo))
        stringo = []

def 

def hi_back():
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    alen = len(alphabet)
    user = input("Give me something ")
    hellow = [8, 5, 12, 12, 15, 0, 23, 15, 18, 12, 4]  
    hellop = [8, 5, 12, 12, 15, 0, 16, 5, 18, 19, 15, 14]
    vals = []
    for letter in user:
        vals.append(alphabet.index(letter.lower()))

    tals = [alphabet.index(letter.lower()) for letter in "Hello Person"]

    oal = []
    for i in range(len(vals)):
        # check if bumps added value to a list place. So similar to number places.
        if (i+1) > len(oal):
            total = val[i]
        else: 
            total = val[i] + oal[i]

        # if certain numbers hit apply 
        if total == 23:
            total += 20
        elif total == 16:
            total += 11 + (27 * 27) #
        elif total == 45:
            total += 
        elif val[i] == 4:
            total += 10

        bumps = total // alen
        total = total % alen
        for x in range(bumps):
            if x+1 == bumps:
                oal.append(bumps)
            else:
                oal.append(0)
        oal.append(total)


    print(vals, tals)

hi_back()    
