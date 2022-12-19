
def main():
    items = 0
    maxItem = 0
    topThree = 0
    
    with open('day1input.txt') as f:
        lines = f.readlines()
        f.close()
    
    myArr = []
    for line in lines:
        if line.strip() != "":   
            items += int(line)
        if line.strip() == "":  
            myArr.append(items)
            items = 0
    
    myArr.sort(reverse=True)
    for arr in range(3):
        topThree += myArr[arr]
        
    print("Top three items: ", topThree)
                
 
 
    
if __name__ == "__main__":
    main()