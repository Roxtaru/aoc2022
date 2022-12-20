def main():
    arr = []
    foundSame = []
    totalPrior = 0
    charFound = False
    i = 0
    with open("day3input.txt") as f:
        lines = f.readlines()
        f.close()
        
    while i < len(lines):
        item1 = lines[i]
        item2 = lines[i+1]
        item3 = lines[i+2]
        
        for k in range(len(item1)):
            for j in range(len(item2)):
                if item1[k] == item2[j]:
                    arr.append(item2[j])
        
        for k in range(len(item3)):
            for a in arr:
                if item3[k] == a and charFound == False:
                    foundSame.append(a)
                    charFound = True
                    arr = []
        
        i += 3
        charFound = False

    
    print(foundSame)  
    for a in foundSame:
        charInt = ord(a)
        if charInt > 96:
            charInt -= 96
        if charInt > 64 and charInt < 91:
            charInt -= 38
        totalPrior += charInt
        
    print(totalPrior)
    
    
    
if __name__ == "__main__":
    main()