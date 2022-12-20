
def main():
    arr = []
    totalPrior = 0
    charFound = False
    with open("day3input.txt") as f:
        lines = f.readlines()
        f.close()
        
    for line in lines:
        strLen = len(line)/2
        strLen2 = len(line)
        comp1 = line[0 : int(strLen)]
        comp2 = line[int(strLen) : int(strLen2)]
        for i in range(len(comp1)):
            for j in range(len(comp2)):
                if comp1[i] == comp2[j] and charFound == False:
                    arr.append(comp1[i])
                    charFound = True
        charFound = False
        
    for a in arr:
        charInt = ord(a)
        if charInt > 96:
            charInt -= 96
        if charInt > 64 and charInt < 91:
            charInt -= 38
        totalPrior += charInt
        
    print(totalPrior)
    
    
    
if __name__ == "__main__":
    main()