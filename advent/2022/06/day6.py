import ctools

def main():
    data = ctools.wopen('day6.d')
    tote = []
    for x, character in enumerate(data):
        if x < 3:
            tote += [character]
        tote += [character]
        #if len(set(tote)) == 4:
            #print(tote)
            # remember, it must be after the 4 unique characters.
            #print(x+1, "is the start-of-packet marker")
            #return x
        tote.pop(0)
        
    tote2 = []
    for x, character in enumerate(data):
        if x+1 < 14:
            tote2 += [character]
        tote2 += [character]
        if len(set(tote2)) == 14:
            print(tote2)
            print(x + 1, "is the first start of message marker")
            return x
        tote2.pop(0)


    print("success")
if __name__ == "__main__":
    main()
        
